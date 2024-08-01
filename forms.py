from django import forms
from main.models import Nota

class NotaModelForm(forms.ModelForm):

  class Meta:
    model = Nota
    fields = ['nombre', 'email', 'tipo']

    widgets = {
      'nombre': forms.TextInput(
        attrs={
          'class': 'form-control',
          'type': 'text'
        }
      ),
      'email': forms.EmailInput(
        attrs={
          'class': 'form-control',
          'type': 'email'
        }
      ),
      'tipo': forms.Select(
        attrs={
          'tipo': 'form-select',
        }
      ),
    }