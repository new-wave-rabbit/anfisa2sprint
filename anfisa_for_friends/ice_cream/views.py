from django.shortcuts import render
from ice_cream.models import IceCream

def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    context = {}
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    ice_cream_list = IceCream.objects.all()
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
