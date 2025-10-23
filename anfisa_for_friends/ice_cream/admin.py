from django.contrib import admin

# Register your models here.
from .models import Category, IceCream, Topping, Wrapper

admin.site.empty_value_display = 'Не задано'

admin.site.register(Topping)
admin.site.register(Wrapper)

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'output_order',
    )
    list_editable = (
        'slug',
        'output_order',
    )
    search_fields = ('title',)
    list_filter = ('title',)
    list_display_links = ('title',)
# Регистрируем кастомное представление админ-зоны
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
