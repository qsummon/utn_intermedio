from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    # title = models.CharField(max_length=100)
    # subtitle = models.CharField(max_length=100, default='')
    # content = models.TextField()

    # testing verbose
    # titulo = models.CharField(max_length=100, verbose_name='TESTING')
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, default='')
    contenido = models.TextField()

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'nota'
        verbose_name_plural = 'notas'
    # def get_model_fields(model):
    #     return model._meta.fields
