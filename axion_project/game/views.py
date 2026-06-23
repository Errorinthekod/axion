from django.http import HttpResponse
from django.shortcuts import render

from .models import Category


# Create your views here.

def category_view(request):

    queryset = Category.objects.all()
    return HttpResponse(queryset)


