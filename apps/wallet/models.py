from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


CURRENCY = (
       ('Bitcoin', 'Bitcoin'),
       ('Ethereum', 'Ethereum'),
       ('Litecoin', 'Litecoin'),
       ('Dai', 'Dai'),   
   )

SYMBOLS = (
       ('BTC', 'BTC'),
       ('ETH', 'ETH'),
       ('LTC', 'LTC'),
       ('DAI', 'DAI'),   
   )

class Currency(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, choices=CURRENCY, default=1,)
    symbol = models.CharField(max_length=50, choices=SYMBOLS, default=1,)
    value = models.DecimalField(max_digits=19,  decimal_places=8, blank=True, null=True)
    private_key = models.CharField(max_length=300)
    public_key = models.CharField(max_length=300)
    address =  models.CharField(max_length=300, blank=True)
    enabled = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'symbol', 'value', 'address','enabled')


class Wallet(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20,  decimal_places=2, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'amount')

class ConnectoWalletCurrency(models.Model):
    id_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    id_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=30,  decimal_places=8, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class ConnectoWalletCurrencyAdmin(admin.ModelAdmin):
    list_display = ('id_wallet', 'id_currency', 'amount', 'createdAt')