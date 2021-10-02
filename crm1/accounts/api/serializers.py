from rest_framework import serializers
from accounts.models import *

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
        
    
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        