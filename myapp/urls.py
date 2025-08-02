from . import views
from django.urls import path
urlpatterns=[path('',views.home,name='home'),
             path('home2',views.home2,name='home2'),
             path('verify2',views.verif,name='verify')]