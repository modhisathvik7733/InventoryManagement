# Generated by Django 4.1.6 on 2023-02-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory_app", "0006_order_orderitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="complete",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
