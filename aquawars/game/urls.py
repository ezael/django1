from django.urls import path
from game import views

urlpatterns = [
    path('', views.index, name='index'),
    path('construction/', views.construction, name='construction'),
    path('recherche/', views.recherche, name='recherche'),
    path('navire/', views.navire, name='navire'),
    path('flotte/', views.flotte, name='flotte'),
    path('commerce/', views.commerce, name='commerce'),
    path('new_account/', views.new_account, name='new account'),
]
