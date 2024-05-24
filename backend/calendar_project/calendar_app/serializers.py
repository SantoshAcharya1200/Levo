# calendar_app/serializers.py

from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)

    class Meta:
        model = Event
        fields = ['id', 'title', 'start_time', 'end_time', 'description', 'participants']
        read_only_fields = ['id']

    def create(self, validated_data):
        participants = validated_data.pop('participants', [])
        event = Event.objects.create(**validated_data)
        event.participants.set(participants)
        return event
