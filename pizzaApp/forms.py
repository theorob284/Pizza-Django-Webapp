from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Pizza, Topping, Size, Crust, Sauce, Cheese

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PizzaForm(forms.ModelForm):
    toppings = forms.ModelMultipleChoiceField(
        queryset=Topping.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Pizza
        fields = ["name", "size", "crust", "sauce", "cheese", "toppings"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Pizza Name"}),
            "size": forms.Select(attrs={"class": "form-control"}),
            "crust": forms.Select(attrs={"class": "form-control"}),
            "sauce": forms.Select(attrs={"class": "form-control"}),
            "cheese": forms.Select(attrs={"class": "form-control"}),
        }