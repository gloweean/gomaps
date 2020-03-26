from ..serializers.orders import OrderSerializer
from rest_framework import generics, permissions, authentication
from utils.permissions import IsOrderOwner
from ..models import Order


__all__ = [
    'OrderListCreateView',
    'OrderRetrieveUpdateDestroyView'
]


class OrderListCreateView(generics.ListCreateAPIView):
    '''
    GET PUT
    '''
    queryset = Order.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        user = self.request.user
        return user.order_set.all()


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    '''
    GET PUT PATCH DELETE
    '''
    queryset = Order.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOrderOwner
    )

    serializer_class = OrderSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return user.order_set.all()