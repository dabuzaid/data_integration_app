from rest_framework import serializers
from .models import Customer, Salesman, SalesM, SalesD, ItemCard, \
    CustCard,SalesMIntegration,Receipt,TransferM,TransferD,ReceiveM,ReceiveD,VoucherHead,VoucherDet
#SuppCard


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SalesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        fields = '__all__'


class SalesMSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesM
        fields = '__all__'


class SalesDSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesD
        fields = '__all__'


class ItemCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCard
        fields = '__all__'


class CustCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustCard
        fields = '__all__'


class SalesMIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesMIntegration
        fields = '__all__'

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'

class TransferMSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferM
        fields = '__all__'

class TransferDSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferD
        fields = '__all__'

class ReceiveMSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiveM
        fields = '__all__'

class ReceiveDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiveD
        fields = '__all__'



class VoucherHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherHead
        fields = '__all__'

class VoucherDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherDet
        fields = '__all__'

class VoucherHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherHead
        fields = '__all__'

class VoucherDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherDet
        fields = '__all__'