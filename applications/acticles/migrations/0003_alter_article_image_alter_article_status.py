# Generated by Django 4.1.7 on 2023-03-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acticles', '0002_alter_article_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='articles'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], max_length=6),
        ),
    ]