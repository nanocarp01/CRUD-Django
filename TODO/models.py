from django.db import models

class Tarea(models.Model):
    tarea = models.CharField(max_length=100)
    descr = models.TextField(max_length=500, blank=True, null=True)
    
    
    def __str__(self):
        return self.tarea
