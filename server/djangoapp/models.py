# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Name of the car make")
    description = models.TextField(blank=True, help_text="Description of the car make")
    country_of_origin = models.CharField(max_length=100, blank=True, help_text="Country where the car make originated")
    year_established = models.PositiveIntegerField(null=True, blank=True, help_text="Year the car make was established")

    def __str__(self):
        return f"{self.name} ({self.year_established if self.year_established else 'Unknown'})"



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Define CarModel model
class CarModel(models.Model):
    # Choices for car type
    CAR_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
    ]

    # Fields for CarModel
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='car_models')  # Many-to-one relationship
    dealer_id = models.IntegerField()  # Refers to a dealer in Cloudant DB
    name = models.CharField(max_length=100)  # Name of the car model
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)  # Type of car with limited choices
    year = models.DateField()  # Year of manufacture
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional field for price
    color = models.CharField(max_length=30, null=True, blank=True)  # Optional field for color

    def __str__(self):
        return f"{self.car_make} {self.name} ({self.year.year})"
