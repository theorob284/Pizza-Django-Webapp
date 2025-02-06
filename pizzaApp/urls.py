from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('contact/', views.contact, name="contact"),
   path('login/', views.user_login, name="login"),
   path('logout/', views.user_logout, name="logout"),
   path('register/', views.register, name="register"),
   path("create-pizza/", views.create_pizza, name="create_pizza"),
   path("pizzas/", views.pizza_list, name="pizza_list"),
]

