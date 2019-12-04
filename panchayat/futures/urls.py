from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


from django.conf.urls import url,include 

urlpatterns = [
    path('', home, name="home"),
    path('new_futures/', new_futures, name="new_futures"),
    path('new_market/',new_market_order, name="new_market"),
    path('portfolio_market/',portfolio_market, name="new_market"),
    url(r'^sell_market/(?P<order_id>[0-9]+)$', sell_market, name='panel_person_form'),
    



]   