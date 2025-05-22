from django.urls import path
from .views import GetCounter, UpdateCounter

urlpatterns = [
    path('api/counter/', GetCounter.as_view()),
    path('api/counter/<str:action>/', UpdateCounter.as_view()),
]