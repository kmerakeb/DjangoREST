from rest_framework import serializers
from .models import Business, Service


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('pk', 'business', 'service_name', 'service_category', 'service_image', 'serivce_duration', 'service_description', 'service_price', 'rating')


class BusinessSerializer(serializers.ModelSerializer):
    #services = ServiceSerializer(many=True, read_only=True)
    class Meta:
        model = Business
        fields = ('pk', 'business_logo','user','business_name', 'business_id', 'price', 'city', 'state', 'address', 'date_created', 'date_updated', 'business_categories')

        def perform_create(self, serializer):  # new
            serializer.save(owner=self.request.user)


