from django.db import models
from django.contrib.auth.models import User

class Size(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Crust(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Sauce(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Cheese(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.size.name}, {self.crust.name})"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link payment to user
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    card_number = models.CharField(max_length=16)  # Store only last 4 digits for security
    card_expiry = models.CharField(max_length=5)   # Format: MM/YY
    card_cvv = models.CharField(max_length=3)      # Store securely in production
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.user.username} - {self.full_name}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    card_number = models.CharField(max_length=16)  # Normally should be encrypted
    expiry_date = models.CharField(max_length=5)  # MM/YY format
    cvv = models.CharField(max_length=3)  # Security code

    def __str__(self):
        return f"Payment by {self.name} for Pizza {self.pizza.id}"
