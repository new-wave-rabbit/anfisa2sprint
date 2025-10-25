from django.shortcuts import render
from ice_cream.models import IceCream
# Для применения Q-объектов их нужно импортировать:
from django.db.models import Q

def index(request):
    template_name = 'homepage/index.html'
    # Запрос:
    ice_cream_list = IceCream.objects.values(
        'id', 'title'
    ).filter(
        # Делаем запрос, объединяя два условия
        # через Q-объекты и оператор AND:
        Q(is_published=True) & Q(is_on_main=True)
    ).order_by('title')[1:4]
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)