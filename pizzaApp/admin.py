from django.contrib import admin
from .models import Pizza, Topping, Size, Crust, Sauce, Cheese

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Size)
admin.site.register(Crust)
admin.site.register(Sauce)
admin.site.register(Cheese)
