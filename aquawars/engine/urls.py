from django.urls import path
from engine import views

urlpatterns = [
    path('', views.engine, name='engine'),
]
