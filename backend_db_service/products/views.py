from django.shortcuts import render
from .models import Products
from .serializers import ProductsSerializer
from rest_framework import generics
# Create your views here.



class ProductsInfo(generics.ListAPIView):
    queryset= Products.objects.all()
    serializer_class= ProductsSerializer