# Generated by Django 3.0.11 on 2021-01-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_blog', '0002_auto_20210104_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]