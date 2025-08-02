from django.urls import path
from . import views
urlpatterns=[
    path('',views.register,name="register"),
    path('register',views.register),
    path('login/',views.login_f),
    path('todo',views.todo,name='todo'),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('edit/<int:id>/edit',views.edit),
    path('logout',views.signout,name="logout"),
    path('login/login',views.login_f)
   
]