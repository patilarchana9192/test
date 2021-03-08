from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.Signup.as_view()),# path=user/signup
    path('login', views.Login.as_view()),# path=user/login
    path('logout', views.Logout.as_view()),# path=user/logout
    path('subscription',views.Payment.as_view()),# path=user/subscription
    ]