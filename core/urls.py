from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('details/<int:id>',details,name='details'),
    path('new_debt/',new_debt,name="new_debt"),
]