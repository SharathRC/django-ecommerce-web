# Generated by Django 4.2.4 on 2023-08-19 10:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_alter_category_options_product"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ("-created_at",)},
        ),
    ]
