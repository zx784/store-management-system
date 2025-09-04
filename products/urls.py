from .views import *
from django.urls import path

urlpatterns = [
    path('products/', ProudcutlistView.as_view(), name = 'product-list'),
    path('products/create/', Productcreatlist.as_view(), name= 'product-create'),
    path('products/view/', productuserview.as_view(), name= 'product-view'),
    path('products/<int:pk>/update/', productupdate.as_view(), name= 'product-update'),
    path('products/<int:pk>/delate/', productdelate.as_view(), name= 'product-delate'),
]


