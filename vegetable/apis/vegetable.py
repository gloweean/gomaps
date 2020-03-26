from ..serializers.vegetables import VegetableSerializer
from rest_framework import generics, permissions, authentication
from ..models import Vegetable

__all__ = [
    'VegetableListCreateView',
    'VegetableRetrieveUpdateDestroyView',
]


class VegetableListCreateView(generics.ListCreateAPIView):
    '''
    GET POST
    '''
    queryset = Vegetable.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VegetableSerializer
    

class VegetableRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    '''
    GET PUT PATCH DELETE
    '''
    queryset = Vegetable.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = VegetableSerializer
    lookup_field = 'id'