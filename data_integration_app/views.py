from django.shortcuts import render

from rest_framework import viewsets

from .models import Customer, Salesman, SalesM, SalesD, ItemCard, CustCard, \
    SalesMIntegration, Receipt, TransferM, TransferD, ReceiveM, ReceiveD,SuppCard, VoucherHead, VoucherDet
from .serializers import CustomerSerializer, SalesmanSerializer, SalesMSerializer, \
    SalesDSerializer, ItemCardSerializer, CustCardSerializer, \
    SalesMIntegrationSerializer, ReceiptSerializer, TransferMSerializer, \
    TransferDSerializer, ReceiveMSerializer, ReceiveDSerializer,SuppCardSerializer, VoucherHeadSerializer, VoucherDetSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SalesmanViewSet(viewsets.ModelViewSet):
    queryset = Salesman.objects.all()
    serializer_class = SalesmanSerializer

class SalesMViewSet(viewsets.ModelViewSet):
    queryset = SalesM.objects.all()
    serializer_class = SalesMSerializer

class SalesDViewSet(viewsets.ModelViewSet):
    queryset = SalesD.objects.all()
    serializer_class = SalesDSerializer

class ItemCardViewSet(viewsets.ModelViewSet):
    queryset = ItemCard.objects.all()
    serializer_class = ItemCardSerializer

class CustCardViewSet(viewsets.ModelViewSet):
    queryset = CustCard.objects.all()
    serializer_class = CustCardSerializer

class SalesMIntegrationViewSet(viewsets.ModelViewSet):
    queryset = SalesMIntegration.objects.all()
    serializer_class = SalesMIntegrationSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

class TransferMViewSet(viewsets.ModelViewSet):
    queryset = TransferM.objects.all()
    serializer_class = TransferMSerializer

class TransferDViewSet(viewsets.ModelViewSet):
    queryset = TransferD.objects.all()
    serializer_class = TransferDSerializer

class ReceiveMViewSet(viewsets.ModelViewSet):
    queryset = ReceiveM.objects.all()
    serializer_class = ReceiveMSerializer

class ReceiveDViewSet(viewsets.ModelViewSet):
    queryset = ReceiveD.objects.all()
    serializer_class = ReceiveDSerializer

class SuppCardViewSet(viewsets.ModelViewSet):
    queryset = SuppCard.objects.all()
    serializer_class = SuppCardSerializer

class VoucherHeadViewSet(viewsets.ModelViewSet):
    queryset = VoucherHead.objects.all()
    serializer_class = VoucherHeadSerializer

class VoucherDetViewSet(viewsets.ModelViewSet):
    queryset = VoucherDet.objects.all()
    serializer_class = VoucherDetSerializer