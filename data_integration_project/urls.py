
from django.urls import path
from django.shortcuts import render
#from data_integration.data_integration_app.views import CustomerViewSet, SalesmanViewSet, SalesMViewSet, SalesDViewSet, ItemCardViewSet, CustCardViewSet

from data_integration_app.views import (CustomerViewSet, SalesmanViewSet, SalesMViewSet,
                                        SalesDViewSet, ItemCardViewSet, CustCardViewSet,
                                        SalesMIntegrationViewSet,ReceiptViewSet)

from django.http import HttpResponse

from data_integration_app.views import TransferMViewSet, TransferDViewSet, ReceiveMViewSet, \
    ReceiveDViewSet, VoucherHeadViewSet, VoucherDetViewSet


def home(request):
    return render(request, 'main.html')
    #return HttpResponse("Batook IT -- Data Integration")

urlpatterns = [
    path('', home, name='home'),
    path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customer-list'),
    path('customers/<int:pk>/',
         CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='customer-detail'),

    path('salesmen/', SalesmanViewSet.as_view({'get': 'list', 'post': 'create'}), name='salesman-list'),
    path('salesmen/<int:pk>/',
         SalesmanViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='salesman-detail'),

    path('salesm/', SalesMViewSet.as_view({'get': 'list', 'post': 'create'}), name='salesm-list'),
    path('salesm/<int:pk>/',
         SalesMViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='salesm-detail'),

    path('salesd/', SalesDViewSet.as_view({'get': 'list', 'post': 'create'}), name='salesd-list'),
    path('salesd/<int:pk>/',
         SalesDViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='salesd-detail'),

    path('itemcard/', ItemCardViewSet.as_view({'get': 'list', 'post': 'create'}), name='itemcard-list'),
    path('itemcard/<int:pk>/',
         ItemCardViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='itemcard-detail'),

    path('custcard/', CustCardViewSet.as_view({'get': 'list', 'post': 'create'}), name='custcard-list'),
    path('custcard/<int:pk>/',
         CustCardViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='custcard-detail'),

    path('salesmintegration/', SalesMIntegrationViewSet.as_view({'get': 'list', 'post': 'create'}), name='salesm-list'),



path('transferm/', TransferMViewSet.as_view({'get': 'list', 'post': 'create'}), name='transferm'
                                                                                     '-list'),
    path('transferd/', TransferDViewSet.as_view({'get': 'list', 'post': 'create'}), name='transferd'
                                                                                     '-list'),
    path('receivem/', ReceiveMViewSet.as_view({'get': 'list', 'post': 'create'}), name='receivem'
                                                                                     '-list'),
    path('received/', ReceiveDViewSet.as_view({'get': 'list', 'post': 'create'}), name='received'
                                                                                     '-list'),
    path('voucherhead/', VoucherHeadViewSet.as_view({'get': 'list', 'post': 'create'}), name='voucherhead'
                                                                                     '-list'),
    path('voucherdet/', VoucherDetViewSet.as_view({'get': 'list', 'post': 'create'}), name='voucherdet'
                                                                                     '-list'),


]
