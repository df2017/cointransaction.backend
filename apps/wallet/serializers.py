from rest_framework import serializers
from apps.wallet.models import Currency, Wallet, ConnectoWalletCurrency
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from bitcoin import pubtoaddr, random_key, privtopub
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        managed = False
        model = User
        fields = ['id', 'username', 'email',]

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    @transaction.atomic
    def create(self, validated_data): 
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        user_created = User.objects.get(pk=user.pk)
        wallet = Wallet.objects.create(
            name=validated_data['username'],
            owner=user_created,
        )
        wallet.save()

        return user
    
class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = "__all__"


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ['id', 'owner', 'name', 'symbol', 'enabled', "address", "value"]

    @transaction.atomic
    def create(self, validated_data):
        private = random_key()
        public = privtopub(private)
        hash_address = pubtoaddr(public)

        currency = Currency.objects.create(
            owner=validated_data['owner'],
            name=validated_data['name'],
            symbol=validated_data['symbol'],
            private_key=private,
            public_key=public,
            address=hash_address,
            enabled=validated_data['enabled']
        )
        currency.save()

        wallet = Wallet.objects.get(owner=currency.owner)
        connector = ConnectoWalletCurrency.objects.create(
            id_wallet=wallet,
            id_currency=currency,
            amount=wallet.amount
        )
        connector.save()

        return currency

class ConnectoWalletCurrencySerializer(serializers.ModelSerializer):
    id_wallet = WalletSerializer('id_wallet')
    id_currency = CurrencySerializer('id_currency')
    
    class Meta:
        managed = False
        model = ConnectoWalletCurrency
        fields = "__all__"