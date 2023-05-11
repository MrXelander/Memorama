from django.urls import path
from memorama import views

urlpatterns = [
    path('', views.index)
]
