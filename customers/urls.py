from django.urls import path
from .views import *

urlpatterns = [
    path('register/', CustomerRegistrtion.as_view(), name='customer-register'),
    path('customers/', ListAllusers.as_view(), name='customers-list'),
    path('customers/<int:pk>/update/', Updataprofile.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', Deleteaccount.as_view(), name='customer-delete'),
]
