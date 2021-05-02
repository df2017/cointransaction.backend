from django.contrib import admin
from .models import Transaction, TransactionAdmin, TransactionInput, TransactionInputAdmin, TransactionOutput, TransactionOutputAdmin


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionInput, TransactionInputAdmin)
admin.site.register(TransactionOutput, TransactionOutputAdmin)