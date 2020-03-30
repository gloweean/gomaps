from rest_framework import generics, permissions, authentication
from ..serializers.reports import TotalOrderSerializer
from ..models import TotalOrder

__all__ = [
    'TotalOrderListCreateView',
]


class TotalOrderListCreateView(generics.ListCreateAPIView):
    '''
    GET POST
    '''
    queryset = TotalOrder.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = TotalOrderSerializer


class TotalOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    '''
    GET PUT PATCH DELETE
    '''
    queryset = TotalOrder.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = TotalOrderSerializer

    lookup_field = 'id'
