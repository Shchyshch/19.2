from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    changed_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название версии')
    number = models.CharField(max_length=200, verbose_name='Номер версии')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    is_active = models.BooleanField(default=True, verbose_name='Активность версии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


class Material(models.Model):
    name = models.CharField(max_length=200, verbose_name='Заголовок')
    body = models.TextField(**NULLABLE, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='slug')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
