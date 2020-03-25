from rest_framework import generics, permissions
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

    def perform_create(self, serializer):
        instance = serializer.save(email=self.request.POST['email'])
        if serializer._context["request"].FILES is not None:
            img_profile_gen = serializer._context["request"].FILES.values()

            for img_profile in img_profile_gen:
                instance.img_profile = img_profile
                instance.save()
                break


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ObjectIsRequestUser
    )

