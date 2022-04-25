from django.db import models

# Create your models here.
class Premio(models.Model):
    imagen=models.ImageField(upload_to='premios')
    detalles=models.TextField()
