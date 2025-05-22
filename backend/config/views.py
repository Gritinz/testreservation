# backend/config/views.py
from django.http import JsonResponse
from .models import Counter

def get_counter(request):
    counter, created = Counter.objects.get_or_create(id=1)
    return JsonResponse({"value": counter.value})

def increment_counter(request):
    counter, created = Counter.objects.get_or_create(id=1)
    counter.value += 1
    counter.save()
    return JsonResponse({"value": counter.value})

def decrement_counter(request):
    counter, created = Counter.objects.get_or_create(id=1)
    counter.value -= 1
    counter.save()
    return JsonResponse({"value": counter.value})