from django.contrib import admin
from .models import Wallet, WalletAdmin,  Currency , CurrencyAdmin, ConnectoWalletCurrency, ConnectoWalletCurrencyAdmin


admin.site.register(Wallet, WalletAdmin)
admin.site.register(Currency,  CurrencyAdmin)
admin.site.register(ConnectoWalletCurrency,  ConnectoWalletCurrencyAdmin)