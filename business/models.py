from django.db import models
from django.contrib.auth import settings

BUSINESS_CATEGORIES = (
    ('Beauty' , 'Beauty'),
    ('Health', 'Health'),
    ('Relaxation', 'Relaxation'),
    ('Fitness', 'Fitness')

)

class Business(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='businesses', on_delete= models.CASCADE)
    business_logo = models.ImageField(upload_to= 'business_image', null=True, blank=True, width_field= "width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    business_name = models.CharField(max_length=300)
    business_id = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length= 200)
    state = models.CharField(max_length= 100)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add= True)
    date_updated = models.DateTimeField(auto_now= True, blank= True)
    business_categories = models.CharField(max_length= 100, choices = BUSINESS_CATEGORIES)
    #image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field = "width_field", height_field= "height_field")
    #height_field = models.IntegerField(default=0)
    #width_field = models.IntegerField(default=0)


    def __str__(self):
    	return self.business_name


class Service(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    service_name = models.CharField(max_length= 255)
    service_category = models.CharField(max_length=255)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    service_image = models.ImageField(upload_to='service_image', null=True, blank=True, width_field="width_field",
                                      height_field="height_field")
    serivce_duration = models.IntegerField(default=0)
    service_description = models.TextField(max_length= 600, blank= True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    rating = models.FloatField()
    business = models.ForeignKey(Business, related_name='services', on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name