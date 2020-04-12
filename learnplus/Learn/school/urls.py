from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_login, name="guest_login"),
    path('guest_signup', views.guest_signup, name="guests_signup"),
    path('guest_forgot_password', views.guest_forgot_password, name="guest_forgot_password"),
]