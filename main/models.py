from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name="название")
    opisanie = models.TextField(verbose_name="описание", blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    status = models.CharField(max_length=50, default='new', verbose_name="статус")

    def __str__(self):
        return self.name
