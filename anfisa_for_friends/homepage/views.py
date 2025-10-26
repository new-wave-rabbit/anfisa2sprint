from django.shortcuts import render
from ice_cream.models import IceCream
# Для применения Q-объектов их нужно импортировать:
from django.db.models import Q

def index(request):
    template_name = 'homepage/index.html'
    # Запрос:
    # ice_cream_list = IceCream.objects.values(
    #     'id', 'title', 'description', 'category'
    # ).filter(
    #     # Делаем запрос, объединяя два условия
    #     # через Q-объекты и оператор AND:
    #     Q(is_published=True) & Q(is_on_main=True)
    # ).order_by('title')[1:4]
    ice_cream_list = IceCream.objects.select_related('category').filter(
    # Вернуть только те объекты IceCream, у которых
    # в связанном объекте Category в поле is_published хранится значение True:
    category__is_published=True
)

    # ice_cream_list = IceCream.objects.values('id', 'title', 'category__title')

    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)