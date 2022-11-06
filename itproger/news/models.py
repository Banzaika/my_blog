from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=100)
    full_text = models.TextField('Полный текст')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
    def get_absolute_url(self):
        return f'/news/{self.id}'
