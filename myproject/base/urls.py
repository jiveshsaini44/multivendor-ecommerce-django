from django.contrib import admin
from django.urls import path

from base.views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('add_cart/<int:id>/', add_cart, name='add_cart'),
    path('support/',support,name='support'),
    path('knowus/',knowus,name='knowus'),
    path('cart/',cart,name='cart'),
    path('remove/<int:id>/', remove, name='remove'),
    path('increment/<int:id>/', increment, name='increment'),
    path('decrement/<int:id>/', decrement, name='decrement'),
    path('product_details\<int:id>',product_details,name='product_details')
]