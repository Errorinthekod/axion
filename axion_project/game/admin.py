from django.contrib import admin
from .models import Category
# Register your models here.

# Админ панелге кошуу - Добавление в админ панель
admin.site.register(Category)
