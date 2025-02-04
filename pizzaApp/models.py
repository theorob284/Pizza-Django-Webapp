from django.db import models
from django.contrib.auth.models import User

class Topping(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]

    CRUST_CHOICES = [
        ("Thin", "Thin Crust"),
        ("Thick", "Thick Crust"),
        ("Stuffed", "Stuffed Crust"),
        ("Gluten-Free", "Gluten-Free"),
    ]

    SAUCE_CHOICES = [
        ("Tomato", "Tomato Sauce"),
        ("BBQ", "BBQ Sauce"),
        ("Alfredo", "Alfredo Sauce"),
        ("Pesto", "Pesto Sauce"),
    ]

    CHEESE_CHOICES = [
        ("Mozzarella", "Mozzarella"),
        ("Cheddar", "Cheddar"),
        ("Parmesan", "Parmesan"),
        ("Vegan", "Vegan Cheese"),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    crust = models.CharField(max_length=20, choices=CRUST_CHOICES, default="Thin")
    sauce = models.CharField(max_length=20, choices=SAUCE_CHOICES, default="Tomato")
    cheese = models.CharField(max_length=20, choices=CHEESE_CHOICES, default="Mozzarella")
    toppings = models.ManyToManyField(Topping)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_size_display()}, {self.crust} Crust)"