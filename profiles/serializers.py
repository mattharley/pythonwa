from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'name',
            'photo',
            'frontend',
            'backend',
            'year_started_learning',
            'company',
        ]
