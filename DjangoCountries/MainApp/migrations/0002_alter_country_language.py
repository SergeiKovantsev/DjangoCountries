# Generated by Django 4.2.1 on 2023-06-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='language',
            field=models.ManyToManyField(related_name='countries', to='MainApp.language', verbose_name='Языки'),
        ),
    ]