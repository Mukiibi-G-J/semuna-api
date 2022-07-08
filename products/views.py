from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from . import models
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.
class ProductListView(ListAPIView):
    lookup_field = "slug"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product(RetrieveAPIView):
    lookup_field = "slug"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.filter(level=0)
    serializer_class = CategorySerializer


class CategoryItemView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return models.Product.objects.filter(category__slug=self.kwargs["slug"])
        # return models.Product.objects.filter(category__slug=self.kwargs['slug'])

    # def queryset(self):
    #     return models.Product.objects.filter(category__slug=self.kwargs['slug'].get_descendant(include_self=True))


class OrderListView(ListAPIView):
    pass
