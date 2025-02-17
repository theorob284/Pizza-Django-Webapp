from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomLoginForm, RegisterForm, PizzaForm
from django.contrib.auth import authenticate, login, logout
from .models import Pizza, Payment
from django.contrib.auth.decorators import login_required

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

@login_required
def create_pizza(request):
    if request.method == "POST":
        if "name" in request.POST and "card_number" in request.POST:
            name = request.POST.get("name")
            address = request.POST.get("address")
            card_number = request.POST.get("card_number")
            expiry_date = request.POST.get("expiry_date")
            cvv = request.POST.get("cvv")
            pizza_id = request.POST.get("pizza_id")

            # 🔹 Retrieve the pizza instance
            try:
                pizza = Pizza.objects.get(id=pizza_id, created_by=request.user)
            except Pizza.DoesNotExist:
                return render(request, "order.html", {
                    "error": "Pizza not found or access denied."
                })

            # 🔹 Validate payment fields
            if not all([name, address, card_number, expiry_date, cvv]):
                return render(request, "order.html", {
                    "pizza": pizza,
                    "error": "All payment fields are required!"
                })

            # 🔹 Save payment details (Don't store raw card numbers in production!)
            Payment.objects.create(
                user=request.user,
                pizza=pizza,
                name=name,
                address=address,
                card_number=card_number,  # Encrypt this in real-world apps!
                expiry_date=expiry_date,
                cvv=cvv
            )

            # 🔹 Redirect to confirmation page
            return render(request, "order_confirmation.html", {"pizza": pizza})

        # 🔹 If the request is for pizza creation
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.created_by = request.user  # Assign logged-in user
            pizza.save()
            form.save_m2m()

            # 🔹 Redirect to order page with the created pizza
            return render(request, "order.html", {"pizza": pizza})

    else:
        form = PizzaForm()

    return render(request, "create_pizza.html", {"form": form})

@login_required
def pizza_list(request):
    pizzas = Pizza.objects.filter(created_by=request.user)
    return render(request, "pizza_list.html", {"pizzas": pizzas})

