from django.urls import path

from . import views

urlpatterns = [
    path('messallot', views.allot, name='messallot'),
]
