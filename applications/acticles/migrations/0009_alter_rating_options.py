# Generated by Django 4.1.7 on 2023-03-30 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acticles', '0008_rating_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтинги'},
        ),
    ]
