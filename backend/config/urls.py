# backend/config/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/counter', views.get_counter, name='get_counter'),
    path('api/counter/inc', views.increment_counter, name='increment_counter'),
    path('api/counter/dec', views.decrement_counter, name='decrement_counter'),
]