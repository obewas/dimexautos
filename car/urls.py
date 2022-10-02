from django.urls import path

from .views import *

urlpatterns = [ 
    path('update/<pk>/', CarUpdateView.as_view(), name='carUpdate'), 
    path('create', CarCreateView.as_view(), name='carCreate'), 
    path('delete/<pk>/', CarDeleteView.as_view(), name='carDelete'), 
    path('', CarListView.as_view(), name='carList'), 
    path('carDetail/<pk>/', CarDetailView.as_view(), name='carDetail'),

    path('carCost', CarCostView.as_view(), name='carCost'),
    path('costList', CostListView.as_view(), name='costList'),
    path('costUpdate/<pk>/', CostUpdateView.as_view(), name='costUpdate'),
    path('costDetail/<pk>/', CostDetailView.as_view(), name='costDetail'),
    path('costDelete/<pk>/', CostDeleteView.as_view(), name='costDelete'), 

    path('carProfit/<pk>/', CarProfitView.as_view(), name='carProfit'),
 


]
