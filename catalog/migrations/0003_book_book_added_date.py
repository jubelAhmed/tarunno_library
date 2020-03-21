# Generated by Django 3.0.3 on 2020-03-21 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200318_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_added_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
