# Generated by Django 3.2.6 on 2021-09-01 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_company_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='company',
            field=models.ManyToManyField(related_name='related_company', to='games.Company', verbose_name='Компания разработчик'),
        ),
    ]
