from django.urls import path, include
from .import views 
from django.contrib.auth import views as auth_views
from django.conf.urls import url
# from accounts import views as user_views
from .views import *



app_name = "graph"


urlpatterns = [
    path('mystic/', views.mystic, name='mystic'),
    

]