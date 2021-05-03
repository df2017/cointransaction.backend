from rest_framework import serializers
from apps.transaction.models import Transaction, TransactionOutput, TransactionInput
from hashlib import sha256
from bitcoin import ecdsa_sign
from apps.blockchain.models import Block


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id','hash_tx','in_total','out_total','isCoinbase']
        
    
    def create(self, validated_data):
        block = [validated_data['in_total'], validated_data['out_total']]
        hash_generate = sha256(repr(block).encode('utf-8')).hexdigest()
        block = Block.objects.get(id=1)
        tx = Transaction.objects.create(
            block_id=block,
            hash_tx=hash_generate,
            in_total=validated_data['in_total'],
            out_total=validated_data['out_total'],
            isCoinbase=validated_data['isCoinbase'],
        )
        
        tx.save()
        return tx

class TransactionOutputSerializer(serializers.ModelSerializer):
    transaction_id = TransactionSerializer('hash_tx')

    class Meta:
        model = TransactionOutput
        fields = "__all__"
    
    def create(self, validated_data):
        outhash = [validated_data['address'], validated_data['amount'], 
                    validated_data['type_coin'], validated_data['spent']]
        hash_txOut = sha256(repr(outhash).encode('utf-8')).hexdigest()
        txID = validated_data['transaction_id']['hash_tx']
        transaction = Transaction.objects.get(hash_tx=txID)
        txOut = TransactionOutput.objects.create(
            transaction_id=transaction,
            index=validated_data['index'],
            hash_txOut=hash_txOut,
            address=validated_data['address'],
            amount=validated_data['amount'],
            type_coin=validated_data['type_coin'],
            spent=validated_data['spent'],
        )
        txOut.save()
        return txOut

class TransactionInputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransactionInput
        fields = "__all__"
    
    def create(self, validated_data):
        inhash = [validated_data['indexIn'], validated_data['amountIn'], validated_data['hash_txOut'],
                        validated_data['type_coin'], validated_data['private']]
        hash_txIn = sha256(repr(inhash).encode('utf-8')).hexdigest()
        sign = ecdsa_sign(hash_txIn, validated_data['private'])

        txIn = TransactionInput.objects.create(
            transaction_id=validated_data['id_tx'],
            index=validated_data['indexIn'],
            txOut_id=validated_data['hash_txOut'],
            hash_txIn=hash_txIn,
            amount=validated_data['amountIn'],
            type_coin=validated_data['type_coin'],
            sigscript=sign
        )
        txIn.save()

        return txIn