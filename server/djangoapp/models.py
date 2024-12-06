# Uncomment the following imports before adding the Model code
from django.db import models


class CarMake(models.Model):
    
    name = models.CharField(
        max_length=100, unique=True, 
        help_text="Name of the car make"
    )
    description = models.TextField(
        blank=True, 
        help_text="Description of the car make"
    )
    country_of_origin = models.CharField(
        max_length=100, 
        blank=True, help_text="Country where the car make originated"
    )
    year_established = models.PositiveIntegerField(
        null=True, 
        blank=True, help_text="Year the car make was established"
    )

    def __str__(self):
        return f"{self.name} ({self.year_established if self.year_established else 'Unknown'})"

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
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE, 
        related_name='car_models'
    ) 
    dealer_id = models.IntegerField()  
    name = models.CharField(max_length=100)  
    car_type = models.CharField(
        max_length=20, 
        choices=CAR_TYPE_CHOICES
    ) 
    year = models.DateField()  
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True
    )  
    color = models.CharField(
        max_length=30, 
        null=True, 
        blank=True
    )  

    def __str__(self):
        return f"{self.car_make} {self.name} ({self.year.year})"
