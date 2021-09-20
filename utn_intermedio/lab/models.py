from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Clase para input de notas
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, default='')
    contenido = models.TextField()

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    # Retorno el reverso con la primary key de la BBDD
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # Metaclass para modificar Post en modelo de datos y presentacion
    class Meta:
        verbose_name = 'nota'
        verbose_name_plural = 'notas'
    # def get_model_fields(model):
    #     return model._meta.fields
