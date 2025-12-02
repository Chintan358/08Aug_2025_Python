from django.urls import path
from myapp.views import *


urlpatterns = [
    path('', index, name='index'),    
    path('accounts',accounts, name='accounts'),
    path('checkout',checkout, name='checkout'),
    path('cart',cart, name='cart'),
    path('compare',compare, name='compare'),
    path('details',details, name='details'),
    path('shop',shop, name='shop'),
    path('wishlist',wishlist, name='wishlist'),
    path('login-register',login_register, name='login-register'),


]

