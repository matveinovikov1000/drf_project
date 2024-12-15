from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course


class User(AbstractUser):
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите ваш Email"
    )
    phone_number = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Введите ваш номер телефона",
    )
    citi = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Введите город пребывания",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите ваш аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = [
            "email",
            "phone_number",
            "citi",
        ]

    def __str__(self):
        return self.email


class Payments(models.Model):
    FIRST_METHOD = "Наличные"
    SECOND_METHOD = "Перевод на счет"

    PAYMENT_METHOD_CHOICES = [
        (FIRST_METHOD, "Наличные"),
        (SECOND_METHOD, "Перевод на счет"),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        related_name="payments",
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Оплаченный курс",
        help_text="Укажите оплаченный курс",
        related_name="payments",
    )
    payment_date = models.DateField(auto_now_add=True)
    payment_amount = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Сумма оплаты",
        help_text="Укажите сумму оплаты",
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default=FIRST_METHOD,
        verbose_name="Способ оплаты",
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = [
            "owner",
            "paid_course",
            "payment_date",
            "payment_amount",
            "payment_method",
        ]

    def __str__(self):
        return f"{self.paid_course}, {self.payment_amount}, {self.owner}"
