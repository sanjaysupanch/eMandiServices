from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


from django.conf.urls import url,include 

urlpatterns = [
    path('', home, name="home"),
    path('new_order/', new_futures, name="new_futures")


]   