# Generated by Django 4.2.2 on 2023-06-28 04:21

from django.db import migrations, models
import register.utils


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='day',
            field=models.DateField(help_text=register.utils.help_day),
        ),
    ]