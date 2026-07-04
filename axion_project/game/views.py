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
    data = {
        "name": "Minecraft",
        "rating": "5.0",
    }
    return render(
        request,
        "browse.html",
        context = data)






