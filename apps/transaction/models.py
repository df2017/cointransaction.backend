from django.db import models
from apps.blockchain.models import Block
from apps.wallet.models import Currency
from django.contrib import admin

STATUS = (
       (1, 'Unconfirmed'),
       (2, 'Confirmed'),  
   )

class Transaction(models.Model):
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE)
    hash_tx = models.CharField(max_length=300)
    in_total = models.DecimalField(max_digits=10,  decimal_places=8)
    out_total = models.DecimalField(max_digits=10,  decimal_places=8)
    count_txOut = models.IntegerField()
    count_txIn = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS, default=1,)
    timestamp = models.DateTimeField(auto_now_add=True)
    isCoinbase = models.BooleanField(default=False)

    def __str__(self):
        return self.hash_tx

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('block_id', 'hash_tx', 'in_total', 'out_total', 'status', 'timestamp')


class TransactionOutput(models.Model):
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    index =  models.IntegerField()
    hash_txOut = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    amount = models.DecimalField(max_digits=30, decimal_places=8)
    type_coin = models.ForeignKey(Currency, on_delete=models.CASCADE)
    spent = models.BooleanField(default=False)

    def __str__(self):
        return self.hash_txOut

class TransactionOutputAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'hash_txOut', 'address', 'amount', 'type_coin', 'spent')


class TransactionInput(models.Model):
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    index =  models.IntegerField()
    txOut_id = models.ForeignKey(TransactionOutput, on_delete=models.CASCADE)
    hash_txIn = models.CharField(max_length=300)
    amount = models.DecimalField(max_digits=30, decimal_places=8)
    type_coin = models.ForeignKey(Currency, on_delete=models.CASCADE)
    sigscript = models.CharField(max_length=300)

    def __str__(self):
        return self.hash_txIn
    
class TransactionInputAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'txOut_id', 'hash_txIn', 'amount', 'type_coin')







    




