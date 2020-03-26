from rest_framework import permissions


class IsOrderOwner(permissions.BasePermission):
    """
    유저가 변경하려는 Order가 자기 자신의 Order인지 검사
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.operator == request.user
        return False


class ObjectIsRequestUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj == request.user
        else:
            return False
        

class IsThisCustomerOperator(permissions.BasePermission):
    """
    유저가 변경하려는 Customer가 해당 Operator(User)의 Customer인지 검사
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.operator == request.user
        return False
