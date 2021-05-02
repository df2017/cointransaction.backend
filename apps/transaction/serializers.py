from rest_framework import serializers
from apps.transaction.models import Transaction, TransactionOutput, TransactionInput


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields ='__all__'

class TransactionOutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransactionOutput
        fields = "__all__" 

class TransactionInputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransactionInput
        fields = "__all__"