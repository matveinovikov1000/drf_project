# Generated by Django 5.1.4 on 2024-12-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lesson",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите название урока",
                        max_length=100,
                        verbose_name="Название урока",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="materials/lesson_preview/",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание",
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "link_video",
                    models.CharField(
                        blank=True,
                        help_text="Укажите ссылку на видео",
                        max_length=200,
                        null=True,
                        verbose_name="Ссылка на видео",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
                "ordering": ["name", "description", "link_video"],
            },
        ),
        migrations.CreateModel(
            name="Course",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите название курса",
                        max_length=100,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="materials/course_preview/",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание",
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "lessons",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Укажите уроки",
                        related_name="courses",
                        to="materials.lesson",
                        verbose_name="Уроки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
                "ordering": ["name", "description"],
            },
        ),
    ]
