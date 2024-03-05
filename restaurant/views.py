from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import *
from rest_framework.viewsets import ModelViewSet

from .serializers import *


def index(request):
    return render(request, "index.html", context={})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
