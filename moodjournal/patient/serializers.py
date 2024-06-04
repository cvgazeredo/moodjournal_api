
from rest_framework import serializers
from django.contrib.auth.models import User
from typing import OrderedDict

from .models import Patient


class UserPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class PatientSerializer(serializers.ModelSerializer):
    user = UserPatientSerializer()

    class Meta:
        model = Patient
        fields = ['user']
