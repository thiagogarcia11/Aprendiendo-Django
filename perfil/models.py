from email.mime import image
from django.db import models

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=200, verbose_name= 'Título')
    desc= models.TextField(verbose_name= 'Descripción')

    created = models.DateTimeField(auto_now_add=True, verbose_name= 'Fecha de cración')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de actualización')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyecto'

    def __str__(self):
        return self.title