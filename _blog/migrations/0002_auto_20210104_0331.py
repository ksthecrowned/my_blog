# Generated by Django 3.0.11 on 2021-01-04 02:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
        ),
    ]
