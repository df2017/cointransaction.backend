from rest_framework import viewsets
from rest_framework import permissions
from apps.blockchain.models import Block
from apps.blockchain.serializers import BlockSerializer

class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = [permissions.IsAuthenticated]
