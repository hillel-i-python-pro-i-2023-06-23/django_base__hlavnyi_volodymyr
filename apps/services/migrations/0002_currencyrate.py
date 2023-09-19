# Generated by Django 4.2.4 on 2023-09-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CurrencyRate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("rate", models.DecimalField(decimal_places=4, max_digits=10)),
                ("last_updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]