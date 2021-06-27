from django.forms import ModelForm
from .models import Remember


class RememberForm(ModelForm):
    class Meta:
        model = Remember
        fields = ['title', 'memo', 'important']