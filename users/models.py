from django.contrib.auth.models import AbstractUser
from django.db import models

from classes.models import Course, Lesson

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="email", help_text="введите адрес электронной почты"
    )
    phone = models.CharField(max_length=20, verbose_name="телефон", **NULLABLE)
    city = models.CharField(max_length=50, verbose_name="город", **NULLABLE)
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="аватарка", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    PAYMENT_METHOD = [
        ("cash", "Наличными"),
        ("card", "Картой"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment", verbose_name="пользователь", **NULLABLE)
    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты", **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс", **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="урок", **NULLABLE)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD, verbose_name="метод оплаты")
    link = models.URLField(max_length=400, verbose_name="Ссылка на оплату", **NULLABLE)
    session_id = models.CharField(max_length=255, verbose_name="Id Сессии", **NULLABLE)

    def __str__(self):
        return {self.user}, {self.date_of_payment}, {self.amount}, {self.course}

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscription", verbose_name="пользователь", **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс", **NULLABLE)

    def __str__(self):
        return {self.user}, {self.course}

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
