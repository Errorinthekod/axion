from django.http import HttpResponse
from django.shortcuts import render
from .models import Category


# Create your views here.

def category_view(request):
    """
    Бүт категорияларды чыгара турган контроллер
    """
    queryset = Category.objects.all()
    return HttpResponse(queryset)





