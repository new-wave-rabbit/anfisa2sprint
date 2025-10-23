from django.contrib import admin

# Register your models here.
from .models import Category

# ...и регистрируем её в админке:
admin.site.register(Category) 