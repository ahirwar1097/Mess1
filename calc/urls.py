from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mess', views.mess, name='mess'),
    path('allot', views.allot, name='allot'),
    path('register', views.register, name='register'),
    path('apply', views.apply, name='apply'),
    path('allot_details', views.allot_details, name='allot_details'),
]