from ..serializers.orders import OrderSerializer
from rest_framework import generics, permissions, authentication, status
from rest_framework.response import Response
from utils.permissions import IsOrderOwner
from ..models import Order
from vegetable.models import Vegetable
from customer.models import Customer
from report.models import TotalOrder
from django.contrib.auth import get_user_model

User = get_user_model()

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
    
    def perform_create(self, serializer):
        deliver_date = serializer.validated_data["deliver_date"]
        target_vege_id = serializer._kwargs["data"]["vegetable_name"]
        customer_id = serializer._kwargs["data"]["customer"]
        
        operator = self.request.auth.user  # instance
        target_vege = Vegetable.objects.get(id=target_vege_id)  # instance
        target_customer = Customer.objects.get(id=customer_id)  # instance
        
        order_unit = serializer.validated_data["order_unit"]
        order_quantity = serializer.validated_data["order_quantity"]
        if TotalOrder.objects.filter(deliver_date=deliver_date).last() is None:
            vegetable_list = Vegetable.objects.all()
            for vegetable in vegetable_list:
                TotalOrder.objects.create(
                    deliver_date=deliver_date,
                    vege_name=vegetable,
                    quantity_bag=0,
                    quantity_ctn=0,
                    quantity_kg=0,
                    quantity_ea=0,
                )
            
        instance = TotalOrder.objects.get(vege_name_id=target_vege_id, deliver_date=deliver_date)
        if order_unit in ["CTN", ]:
            existed_value = instance.quantity_ctn
            instance.quantity_ctn = existed_value + order_quantity
        elif order_unit in ["BAG", ]:
            existed_value = instance.quantity_bag
            instance.quantity_bag = existed_value + order_quantity
        elif order_unit in ["KG", ]:
            existed_value = instance.quantity_kg
            instance.quantity_kg = existed_value + order_quantity
        else:
            existed_value = instance.quantity_ea
            instance.quantity_ea = existed_value + order_quantity
        
        instance.save()
        serializer.save(
            operator=operator,
            vegetable_name=target_vege,
            customer=target_customer,
        )


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
    
    def perform_update(self, serializer):
        # valid test 추가
        
        # Total Order가 받는 before_order의 영향을 역으로 제거
        order_id = self.kwargs["id"]
        before_order = Order.objects.get(id=order_id)
        
        deliver_date_before = before_order.deliver_date
        vege_before = before_order.vegetable_name  # instance
        quantity_brfore = before_order.order_quantity
        unit_before = before_order.order_unit
        
        instance = TotalOrder.objects.get(vege_name=vege_before, deliver_date=deliver_date_before)
        if unit_before in ["CTN", ]:
            existed_value = instance.quantity_ctn
            instance.quantity_ctn = existed_value - quantity_brfore
        elif unit_before in ["BAG", ]:
            existed_value = instance.quantity_bag
            instance.quantity_bag = existed_value - quantity_brfore
        elif unit_before in ["KG", ]:
            existed_value = instance.quantity_kg
            instance.quantity_kg = existed_value - quantity_brfore
        else:
            existed_value = instance.quantity_ea
            instance.quantity_ea = existed_value - quantity_brfore
        instance.save()
        
        # 새로운 order의 영향을 재계산 후 Total Order 입력
        deliver_date = serializer.validated_data["deliver_date"]
        target_vege_id = serializer._kwargs["data"]["vegetable_name"]
        customer_id = serializer._kwargs["data"]["customer"]

        operator = self.request.auth.user  # instance
        target_vege = Vegetable.objects.get(id=target_vege_id)  # instance
        target_customer = Customer.objects.get(id=customer_id)  # instance

        order_unit = serializer.validated_data["order_unit"]
        order_quantity = serializer.validated_data["order_quantity"]
        
        if TotalOrder.objects.filter(deliver_date=deliver_date).last() is None:
            vegetable_list = Vegetable.objects.all()
            for vegetable in vegetable_list:
                TotalOrder.objects.create(
                    deliver_date=deliver_date,
                    vege_name=vegetable,
                    quantity_bag=0,
                    quantity_ctn=0,
                    quantity_kg=0,
                    quantity_ea=0,
                )
                
        instance = TotalOrder.objects.get(vege_name_id=target_vege_id, deliver_date=deliver_date)
        if order_unit in ["CTN", ]:
            existed_value = instance.quantity_ctn
            instance.quantity_ctn = existed_value + order_quantity
        elif order_unit in ["BAG", ]:
            existed_value = instance.quantity_bag
            instance.quantity_bag = existed_value + order_quantity
        elif order_unit in ["KG", ]:
            existed_value = instance.quantity_kg
            instance.quantity_kg = existed_value + order_quantity
        else:
            existed_value = instance.quantity_ea
            instance.quantity_ea = existed_value + order_quantity
        instance.save()
        
        # 주문 정보 수정
        try:
            serializer.save(
                operator=operator,
                vegetable_name=target_vege,
                customer=target_customer,
            )
        except Exception as e:  # Error 시 다시 되돌리기
            instance = TotalOrder.objects.get(vege_name=vege_before, deliver_date=deliver_date_before)
            if unit_before in ["CTN", ]:
                existed_value = instance.quantity_ctn
                instance.quantity_ctn = existed_value + quantity_brfore
            elif unit_before in ["BAG", ]:
                existed_value = instance.quantity_bag
                instance.quantity_bag = existed_value + quantity_brfore
            elif unit_before in ["KG", ]:
                existed_value = instance.quantity_kg
                instance.quantity_kg = existed_value + quantity_brfore
            else:
                existed_value = instance.quantity_ea
                instance.quantity_ea = existed_value + quantity_brfore
            instance.save()

            instance = TotalOrder.objects.get(vege_name_id=target_vege_id, deliver_date=deliver_date)
            if order_unit in ["CTN", ]:
                existed_value = instance.quantity_ctn
                instance.quantity_ctn = existed_value - order_quantity
            elif order_unit in ["BAG", ]:
                existed_value = instance.quantity_bag
                instance.quantity_bag = existed_value - order_quantity
            elif order_unit in ["KG", ]:
                existed_value = instance.quantity_kg
                instance.quantity_kg = existed_value - order_quantity
            else:
                existed_value = instance.quantity_ea
                instance.quantity_ea = existed_value - order_quantity
            instance.save()
            return e
        
    def destroy(self, request, *args, **kwargs):
        # Total Order가 받는 before_order의 영향을 역으로 제거
        order_id = self.kwargs["id"]
        before_order = Order.objects.get(id=order_id)
    
        deliver_date_before = before_order.deliver_date
        vege_before = before_order.vegetable_name  # instance
        quantity_brfore = before_order.order_quantity
        unit_before = before_order.order_unit
    
        instance = TotalOrder.objects.get(vege_name=vege_before, deliver_date=deliver_date_before)
        if unit_before in ["CTN", ]:
            existed_value = instance.quantity_ctn
            instance.quantity_ctn = existed_value - quantity_brfore
        elif unit_before in ["BAG", ]:
            existed_value = instance.quantity_bag
            instance.quantity_bag = existed_value - quantity_brfore
        elif unit_before in ["KG", ]:
            existed_value = instance.quantity_kg
            instance.quantity_kg = existed_value - quantity_brfore
        else:
            existed_value = instance.quantity_ea
            instance.quantity_ea = existed_value - quantity_brfore
        instance.save()
    
        before_order.delete()
        return Response('id:{} - 주문이 삭제되었습니다.'.format(order_id), status=status.HTTP_204_NO_CONTENT)