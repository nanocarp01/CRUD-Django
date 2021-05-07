from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    
    class Meta:# sirve para decir a la clase como comportarse
        model = Tarea
        fields = ['tarea', 'descr'] #esto es la variable tarea q esta en models.py, lo hacemos asi para no repetir codigo
        