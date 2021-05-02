from rest_framework import viewsets
from rest_framework import permissions
from apps.transaction.models import Transaction, TransactionOutput, TransactionInput
from apps.transaction.serializers import TransactionSerializer, TransactionOutputSerializer, TransactionInputSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransactionOutputViewSet(viewsets.ModelViewSet):
    queryset = TransactionOutput.objects.all()
    serializer_class = TransactionOutputSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransactionInputViewSet(viewsets.ModelViewSet):
    queryset = TransactionInput.objects.all()
    serializer_class = TransactionInputSerializer
    permission_classes = [permissions.IsAuthenticated]

