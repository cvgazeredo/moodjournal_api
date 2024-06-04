from django.contrib.auth.models import User

from rest_framework import serializers

from patient.models import Patient
from mood.models import Mood
from .models import Journal


class JournalPatientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class JournalPatientSerializer(serializers.ModelSerializer):
    user = JournalPatientUserSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = ['user']


class JournalMoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ['name']


class JournalSerializer(serializers.ModelSerializer):
    patient = JournalPatientSerializer(read_only=True)
    mood = JournalMoodSerializer(read_only=True)

    class Meta:
        model = Journal
        fields = '__all__'
