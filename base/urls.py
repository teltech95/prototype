from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sample_test/', views.sample_test, name="sample_test"),
    path('farmers/', views.farmers, name="farmers"),
    path('users/', views.users, name="users"),

    path('login/', views.signin, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('doLogin/', views.doLogin, name="doLogin"),


    
    
    # path('doRegister/', views.doRegister, name="doRegister"),
    
]
