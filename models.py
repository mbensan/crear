from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nota(models.Model):
  tipos = (('urgente', 'Urgente'), ('normal', 'Normal'))

  nombre = models.CharField(max_length=100)
  email = models.EmailField(max_length=255)
  tipo = models.CharField(max_length=20, choices=tipos)

class UserProfile(models.Model):
  roles = (('empleado', 'Empleado'), ('jefe', 'Jefe'))
  
  user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
  rol = models.CharField(max_length=100, choices=roles)

  def __str__(self):
    return self.user.username
