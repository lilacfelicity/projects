from django.db import models
from django.utils import timezone

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отложено'),
        ('published', 'Опубликован'),
    )
    category=(
        ('album','Новые альбомы'),
        ('single','Новинки песен'),
        ('videoclip','Обзор на видеоклипы'),
        ('group','Группы'),
        ('article','Статьи'),
    )
    
    title = models.CharField(max_length=250,verbose_name="Заголовок" )
    slug = models.SlugField(max_length=250,verbose_name="Ссылка")
    author = models.CharField(max_length=250,verbose_name="Автор")
    body = models.TextField(max_length=500,verbose_name="Текст")
    categorys=models.CharField(max_length=12,choices=category,default='',verbose_name="Категория")
    picture=models.ImageField(upload_to='KPOP/static/image/',height_field=None,width_field=None,max_length=100,default=None)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Пост был создан в ")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Отложено',verbose_name="Статус")

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE,verbose_name="Пост")
    name = models.CharField(max_length=80,verbose_name="Имя")
    email = models.EmailField(verbose_name="Почта")
    body = models.TextField(verbose_name="Текст")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Комментарий создан в ")
    updated = models.DateTimeField(auto_now=True,verbose_name="Обновлен")
    active = models.BooleanField(default=True,verbose_name="Видимость")

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)