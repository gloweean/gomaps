from ..serializers.customers import CustomerSerializer
from rest_framework import generics, permissions, authentication
from utils.permissions import IsThisCustomerOperator
from ..models import Customer


__all__ = [
    'MyCustomerListCreateView',
    'MyCustomerRetrieveUpdateDestroyView',
]


class MyCustomerListCreateView(generics.ListCreateAPIView):
    '''
    GET POST
    '''
    queryset = Customer.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    serializer_class = CustomerSerializer
    
    def get_queryset(self):
        user = self.request.user
        return user.customer_set.all()
    

class MyCustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    '''
    GET PUT PATCH DELETE
    '''
    queryset = Customer.objects.all()

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsThisCustomerOperator
    )

    serializer_class = CustomerSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return user.customer_set.all()