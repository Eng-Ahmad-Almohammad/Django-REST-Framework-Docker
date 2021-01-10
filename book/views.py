from django.shortcuts import render
# from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from .models import Book
from .serializer  import Bookserializer 
# Create your views here.

class dataView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

class detailsView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

