# Generated by Django 4.2.4 on 2023-09-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0005_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("waiting_approval", "Waiting approval"),
                    ("active", "Active"),
                    ("deleted", "Deleted"),
                ],
                default="active",
                max_length=50,
            ),
        ),
    ]
