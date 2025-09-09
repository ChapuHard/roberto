from django.db import models

class Tarea(models.Model):
    nombre = models.CharField(max_length=255, default='Sin nombre')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre