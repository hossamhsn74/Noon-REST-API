from ..models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # if not declared, all fields of the model will be shown
        fields = ('title', 'descreption', 'price',
                  'category','brand', 'model', 'is_availible', 'is_featured')
