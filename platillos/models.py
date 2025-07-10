from django.db import models

class Platillo(models.Model):
    TIPOS_PLATILLO = [
        ('Bebida', 'Bebida'),
        ('Principal', 'Principal'),
        ('Postre', 'Postre'),
    ]
    DIAS_SEMANA = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
    ]

    dia_semana = models.CharField(max_length=10, choices=DIAS_SEMANA)
    tipo = models.CharField(max_length=10, choices=TIPOS_PLATILLO)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.dia_semana})"

    class Meta:
        ordering = ['dia_semana', 'tipo', 'nombre']
        
        unique_together = ['dia_semana', 'tipo']


class Receta(models.Model):
    platillo = models.OneToOneField(Platillo, on_delete=models.CASCADE, related_name='receta')
    ingredientes = models.TextField()

    def __str__(self):
        return f"Receta de {self.platillo.nombre}"
