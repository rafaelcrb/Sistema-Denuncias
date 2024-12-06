from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['titulo', 'descricao', 'empresa', 'data_incidente', 'denunciante', 'anexo', 'status']
