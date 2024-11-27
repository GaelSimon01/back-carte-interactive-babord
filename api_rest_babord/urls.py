from django.urls import path
from api_rest_babord.views import web_views as views
from django.views.generic import *


urlpatterns = [
    
    path("home/",views.HomeView.as_view(), name='home'),
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),

    path('concerts/', views.ConcertListView.as_view(), name='concerts-list'),
    path('concerts/<int:pk>/', views.ConcertDetailView.as_view(), name='concerts-detail'),
    path('concerts/create/', views.consert_create, name='concerts-create'),
    path('concerts/update/<int:pk>/', views.concert_update, name='concerts-update'),
    path('concerts/delete/<int:pk>/', views.concert_delete, name='concerts-delete'),
]