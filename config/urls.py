"""cointransactionback URL Configuration."""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from apps.wallet.views import RegisterViewSet, WalletViewSet, CurrencyViewSet, UserViewSet, ConnectoWalletCurrencyViewSet
from apps.transaction.views import TransactionViewSet, TransactionOutputViewSet, TransactionInputViewSet, CreateTransaccionBuy
from apps.blockchain.views import BlockViewSet

router = routers.DefaultRouter()

router.register(r'wallet', WalletViewSet)
router.register(r'currency', CurrencyViewSet)
router.register(r'connector', ConnectoWalletCurrencyViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'transactionsout', TransactionOutputViewSet)
router.register(r'transactionsin', TransactionInputViewSet) 
router.register(r'block', BlockViewSet) 
router.register(r'me', UserViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/register/', RegisterViewSet.as_view(), name='auth_register'),
    path('api/v1/buy/', CreateTransaccionBuy.as_view(), name='buy_cripto'),
]