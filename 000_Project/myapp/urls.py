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

    path("user-registration",user_registration,name="user-registration"),
    path("user-login",user_login,name="user-login"),
    path("user-logout",user_logout,name="user-logout"),

    path("getproducts",get_products,name="getproducts"),
    path("getcategories",get_categories,name="getcategories"),
    path("searchproduct",search_product,name="searchproduct"),
    path("addtocart",addtocart,name="addtocart")

]

