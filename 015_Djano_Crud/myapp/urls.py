from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_student, name='register'),
]