# Generated by Django 3.0.11 on 2021-01-08 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_blog', '0025_auto_20210108_0950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='custom',
            options={'ordering': ('title',)},
        ),
        migrations.AddField(
            model_name='custom',
            name='title',
            field=models.CharField(default='Custom', max_length=20),
            preserve_default=False,
        ),
    ]
