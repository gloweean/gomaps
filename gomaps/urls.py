"""gomaps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.apis import obtain_auth_token, UserLogoutView, UserCreateListView, UserRetrieveUpdateDestroyView
from customer.apis import MyCustomerListCreateView, MyCustomerRetrieveUpdateDestroyView
from vegetable.apis import VegetableListCreateView, VegetableRetrieveUpdateDestroyView
from order.apis import OrderListCreateView, OrderRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', UserCreateListView.as_view()),
    path('api/user/login/', obtain_auth_token),
    path('api/user/logout/', UserLogoutView.as_view()),
    path('api/user/<int:id>/', UserRetrieveUpdateDestroyView.as_view()),
    path('api/customer/', MyCustomerListCreateView.as_view()),
    path('api/customer/<int:id>/', MyCustomerRetrieveUpdateDestroyView.as_view()),
    path('api/vegetable/', VegetableListCreateView.as_view()),
    path('api/vegetable/<int:id>/', VegetableRetrieveUpdateDestroyView.as_view()),
    path('api/order/', OrderListCreateView.as_view()),
    path('api/order/<int:id>/', OrderRetrieveUpdateDestroyView.as_view()),
]

