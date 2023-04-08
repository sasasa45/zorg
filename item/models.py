from django.db import models
from django.urls import reverse


# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=256)
    price=models.FloatField()
    sale=models.FloatField(null=True,blank=True)
    slug=models.SlugField(null=True,blank=True)
    video_url=models.URLField(null=True,blank=True)
    description_ru=models.TextField(null=True,blank=True)
    description_ua=models.TextField(null=True,blank=True)
    description_en = models.TextField(null=True, blank=True)
    pdf_1=models.FileField(null=True,blank=True)
    pdf_2=models.FileField(null=True,blank=True)
    pdf_3=models.FileField(null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug})


class Photos(models.Model):
    item=models.ForeignKey(Items, on_delete=models.CASCADE)
    description_ru=models.TextField(null=True,blank=True)
    description_ua=models.TextField(null=True,blank=True)
    description_en = models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to='items')


class ProductCode(models.Model):
    owner=models.CharField(max_length=8, null=True,blank=True)
    code=models.CharField(max_length=8, unique=True)
    date=models.DateField(auto_now_add=True)
    description_ru=models.TextField(null=True,blank=True)
    description_ua=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.owner+' '+self.code


class Spy(models.Model):
    ip=models.CharField(max_length=256)
    slug=models.CharField(max_length=256)
    attempts=models.IntegerField(null=True,blank=True)

    class Meta:
        unique_together=['slug','ip']
