# Generated by Django 5.1.4 on 2024-12-21 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_subscription"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subscription",
            options={
                "ordering": ["courses", "owner"],
                "verbose_name": "Подписка",
                "verbose_name_plural": "Подписки",
            },
        ),
    ]
