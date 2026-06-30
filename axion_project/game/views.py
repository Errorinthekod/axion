from django.http import HttpResponse
from django.shortcuts import render
from .models import Category


# Create your views here.

def category_view(request):
    """
    Бүт категорияларды чыгара турган контроллер (view)
    """
    queryset = Category.objects.all()
    return HttpResponse(queryset)


def game_html(request):
    """
    HTML шаблон чыгара турган контроллер (view)
    """
    data = {}
    return render(request, "browse.html")

#     git checkout main
#     git pull origin  main
#     git checkout -b feature/amir





