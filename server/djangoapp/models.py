# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)

    # Optional extra field: country of origin
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.country})"


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    # Many-to-One relationship: one CarMake can have many CarModels
    car_make = models.ForeignKey('CarMake', on_delete=models.CASCADE)

    # Dealer ID refers to a dealer created in Cloudant database
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100, null=False)

    # Choices for car type
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='Sedan') 
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)],
        default=now().year
    )
    # Optional extra field: color
    # Optional extra field: colorlength=50, blank=True)
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.type}, {self.year})" 