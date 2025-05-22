from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Counter
from .serializers import CounterSerializer

class GetCounter(APIView):
    def get(self, request):
        counter, created = Counter.objects.get_or_create(pk=1)
        serializer = CounterSerializer(counter)
        return Response(serializer.data)

class UpdateCounter(APIView):
    def post(self, request, action):
        try:
            counter = Counter.objects.get(pk=1)
            if action == 'increment':
                counter.count += 1
            elif action == 'decrement':
                counter.count -= 1
            counter.save()
            return Response({'status': 'success'})
        except Counter.DoesNotExist:
            return Response({'error': 'Counter not found'}, status=status.HTTP_404_NOT_FOUND)