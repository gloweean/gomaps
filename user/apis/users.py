from rest_framework import generics, permissions, authentication
from utils.permissions import ObjectIsRequestUser
from django.contrib.auth import get_user_model
from ..serializers import UserSerializer, UserCreateSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny


__all__ = [
    'UserCreateListView',
    'UserRetrieveUpdateDestroyView',
]

User = get_user_model()


class UserCreateListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.object.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        elif self.request.method == 'GET':
            return UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ObjectIsRequestUser
    )

