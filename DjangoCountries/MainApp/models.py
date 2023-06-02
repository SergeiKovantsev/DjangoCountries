from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название страны')
    language = models.ManyToManyField('Language', verbose_name='Языки', related_name='countries')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название языка')

    def __str__(self):
        return self.name
