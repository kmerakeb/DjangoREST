from rest_framework import generics, permissions, filters
from .models import Business, Service
from . import serializers

class BusinessListView(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = serializers.BusinessSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #resource_name = "business"
    filter_backends = (filters.SearchFilter,)
    search_fields = ('business_name',)

class BusinessDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = serializers.BusinessSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ServiceListView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer
   #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ServiceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)