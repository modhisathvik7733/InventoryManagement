# Generated by Django 4.1.6 on 2023-02-09 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
