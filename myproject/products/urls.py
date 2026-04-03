from django.urls import path
from .views import *

urlpatterns = [
    path('vendor_dashboard',vendor_dashboard,name='vendor_dashboard'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:product_id>/',edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('vendor_not_approved',vendor_not_approved,name='vendor_not_approved'),

]

