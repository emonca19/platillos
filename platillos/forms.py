from django import forms
from django.core.exceptions import ValidationError
from .models import Platillo, Receta

class PlatilloForm(forms.ModelForm): 
    class Meta:
        model = Platillo 
        fields = ['dia_semana', 'tipo', 'nombre', 'descripcion', 'precio']

    def clean(self):
        cleaned_data = super().clean()
        dia_semana = cleaned_data.get('dia_semana')
        tipo = cleaned_data.get('tipo')
        
        if dia_semana and tipo:
            existing_platillo = Platillo.objects.filter(dia_semana=dia_semana, tipo=tipo)
            
            if self.instance.pk:
                existing_platillo = existing_platillo.exclude(pk=self.instance.pk)
            
            if existing_platillo.exists():
                platillo_existente = existing_platillo.first()
                raise ValidationError(
                    f'Ya existe un platillo de tipo "{tipo}" para {dia_semana}: '
                    f'"{platillo_existente.nombre}". '
                    f'Solo se permite un platillo de cada tipo por día.'
                )
        
        return cleaned_data


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['ingredientes']
        widgets = {
            'ingredientes': forms.Textarea(attrs={'rows': 6, 'cols': 50}),
        }
