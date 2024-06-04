from rest_framework import serializers
from journal.serializers import JournalPatientSerializer, JournalMoodSerializer
from .models import Mood
from journal.models import Journal


class MoodJournalSerializer(serializers.ModelSerializer):
    patient = JournalPatientSerializer()
    mood = JournalMoodSerializer()

    class Meta:
        model = Journal
        fields = ['text', 'patient', 'mood', 'created_at']


class MoodSerializer(serializers.ModelSerializer):
    journals = MoodJournalSerializer(many=True, read_only=True)

    class Meta:
        model = Mood
        fields = ['name', 'text']
