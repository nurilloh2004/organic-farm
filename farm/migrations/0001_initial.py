# Generated by Django 4.1.2 on 2022-11-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=65)),
                ("value", models.CharField(max_length=550)),
            ],
            options={
                "verbose_name": "Settings",
            },
        ),
    ]
