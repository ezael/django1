from django.urls import path
from game import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_account/', views.new_account, name='new account'),
]
