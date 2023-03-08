from django.forms import ModelForm
from .models import Gassing


class GassingForm(ModelForm):
    class Meta:
        model = Gassing
        fields = ['date', 'gas']