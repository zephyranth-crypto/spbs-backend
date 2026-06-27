# accounts/api/views.py
from rest_framework import generics, permissions
from accounts.models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrAdmin

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdmin]