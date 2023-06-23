# Generated by Django 4.2.1 on 2023-05-23 14:32

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('functional', '0002_country_alter_functional_options_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='functional',
            name='city',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='functional.city'),
        ),
        migrations.AddField(
            model_name='functional',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=2),
        ),
    ]