from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from tinymce import models as tinymce_models


class Items(models.Model):
    name = models.CharField(max_length=256, verbose_name='Назва продукту')
    price = models.FloatField(verbose_name='Ціна')
    sale = models.FloatField(null=True, blank=True, verbose_name='Розпродаж')
    slug = models.SlugField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    description_ru = tinymce_models.HTMLField(null=True, blank=True)
    description_ua = tinymce_models.HTMLField(null=True, blank=True, verbose_name='Опис українською')
    description_en = tinymce_models.HTMLField(null=True, blank=True, verbose_name='Опис англійською')
    pdf_1 = models.FileField(null=True, blank=True, verbose_name='Інструкція українською')
    pdf_2 = models.FileField(null=True, blank=True, verbose_name='Інструкція російською')
    pdf_3 = models.FileField(null=True, blank=True, verbose_name='Інструкція англійською')
    qty = models.IntegerField(default=0, verbose_name='Наявна кількість')

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Продукція'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug})


class Photos(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    description_ru = models.TextField(null=True, blank=True, verbose_name='Опис російською')
    description_ua = models.TextField(null=True, blank=True, verbose_name='Опис українською')
    description_en = models.TextField(null=True, blank=True, verbose_name='Опис англійською')
    image = models.ImageField(upload_to='items', verbose_name='Зображення')

    def __str__(self):
        return f'{self.item.name} {self.description_en }'


class ProductCode(models.Model):
    owner = models.CharField(max_length=8, null=True, blank=True)
    code = models.CharField(max_length=8, unique=True)
    date = models.DateField(auto_now_add=True)
    description_ru = models.TextField(null=True, blank=True)
    description_ua = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.owner} {self.code}'


class Spy(models.Model):
    ip = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    attempts = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ['slug', 'ip']


class Parts(models.Model):
    item = models.ManyToManyField(Items)
    name = models.CharField(max_length=256, verbose_name='Назва', unique=True)
    picture = models.ImageField(upload_to='parts', verbose_name='Зображення')
    url_1 = models.URLField(null=True, blank=True, verbose_name='Посилання №1')
    url_2 = models.URLField(null=True, blank=True, verbose_name='Посилання №2')
    price = models.FloatField(null=True, blank=True, verbose_name='Ціна за одиницю')
    qty = models.IntegerField(verbose_name='Кількість на складі')

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Комплектуючі'

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.picture))
    image_tag.short_description = 'Image'

    def get_items(self):
        return ', '.join([item.name for item in self.item.all()])
    get_items.short_description = 'Освітлювачі'

    def __str__(self):
        return self.name
