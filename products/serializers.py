from rest_framework import serializers
from .models import  Category, Product, ProductImage


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image", "alt_text"]

class ProductSerializer(serializers.ModelSerializer):
    product_image = ImagesSerializer(many=True, read_only=True)
    class Meta:
        model =Product
        fields = ['id', 'category', 'title', 'description', 'slug', 'regular_price','product_image', 'brand']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields =['name', 'slug']



