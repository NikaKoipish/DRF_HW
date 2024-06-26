from django.db import models

from config.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):

    title = models.CharField(max_length=150, verbose_name="название курса")
    preview = models.ImageField(
        upload_to="courses/previews", verbose_name="превью курса", **NULLABLE
    )
    description = models.TextField(verbose_name="описание курса")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name="Создатель")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):

    title = models.CharField(max_length=150, verbose_name="название урока")
    description = models.TextField(verbose_name="описание урока")
    preview = models.ImageField(
        upload_to="lessons/previews", verbose_name="превью урока", **NULLABLE
    )
    video = models.URLField(verbose_name="видео урока", **NULLABLE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="курс"
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name="Создатель")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
