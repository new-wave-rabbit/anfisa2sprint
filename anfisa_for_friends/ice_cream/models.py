from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения',
        default=100,
        )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Topping(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'топпинги'
        verbose_name_plural = 'Топпинги'

class Wrapper(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'обёртки'
        verbose_name_plural = 'Обёртки'

class IceCream(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обертка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping, verbose_name='Топпинг')
    is_on_main = models.BooleanField(default=False, verbose_name='На главную')

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'Мороженое'
