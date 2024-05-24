from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets,status
from .models import Event
from .serializers import EventSerializer
from rest_framework import serializers
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .tasks import send_event_notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        event = serializer.save()
        send_event_notification.apply_async(
            args=[self.request.user.email],
            eta=event.start_time
        )
@api_view(['GET'])
def get_holidays(request):
    countryCode = request.GET.get('countryCode','US')
    year = request.GET.get('year', '2024')  # Default to the current year if not provided

    if not countryCode:
        return Response({'error': 'Country is required'}, status=400)

    url = f'https://date.nager.at/api/v3/publicholidays/{year}/{countryCode}'
    response = requests.get(url)

    if response.status_code != 200:
        return Response({'error': 'Failed to fetch holidays'}, status=response.status_code)

    holidays = response.json()
    return Response(holidays)

@api_view(['GET'])
def test_celery(request):
    send_event_notification.delay('santosh.acharya1201@gmail.com', 'Test Event')
    return Response({'message': 'Task has been sent'}, status=status.HTTP_200_OK)