from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BookSerializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Book
# Create your views here.
class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class=BookSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
