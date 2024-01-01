from django.db import models

# Create your models here.
class Vehicles(models.Model):
    name=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    number=models.CharField(max_length=200)
    km_driven=models.CharField(max_length=200)
    options=(('petrol','petrol'),('diesel','diesel'),('ev','ev'),('cng','cng'))
    fuel_type=models.CharField(max_length=200,choices=options,default='petrol')
    owner=models.CharField(max_length=200)
    condition=models.CharField(max_length=200)
    date_of_purchase=models.CharField(max_length=200)
    owner_type=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    options=(('available','available'),('sold','sold'))
    status=models.CharField(max_length=200,choices=options,default='available')
    
    def __str__(self):
        return self.name



