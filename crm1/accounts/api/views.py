from django.shortcuts import render
from accounts.models import Customer,Product,Order
from accounts.api.serializers import CustomerSerializers,ProductSerializers,OrderSerializers
from rest_framework import generics

class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

class customerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers    

class productListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
class productView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers    

class orderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

class orderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers    