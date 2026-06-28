# accounts/api/serializers.py
from rest_framework import serializers
from accounts.models import User  # import from parent app

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'is_provider', 'created_at']
        read_only_fields = ['id', 'created_at']