from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomLoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from .forms import PizzaForm
from .models import Pizza

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def user_login(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = CustomLoginForm()
    
    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("home")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {"form": form})

def create_pizza(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)  # Don't save to DB yet
            pizza.created_by = request.user  # Assign logged-in user
            pizza.save()  # Save to DB
            return redirect("pizza_list")  # Redirect to pizza list
    else:
        form = PizzaForm()

    return render(request, "create_pizza.html", {"form": form})

def pizza_list(request):
    pizzas = Pizza.objects.all()  # Get all pizzas
    return render(request, "pizza_list.html", {"pizzas": pizzas})