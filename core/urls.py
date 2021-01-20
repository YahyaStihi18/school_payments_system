from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('subscribers/',views.subscribers,name='subscribers'),
    path('details/<int:id>/',views.details,name='details'),
    path('new_debt/',views.new_debt,name="new_debt"),
]
