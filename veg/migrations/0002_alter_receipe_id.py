# Generated by Django 4.2.5 on 2023-10-02 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("veg", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipe",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
