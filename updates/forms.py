from django import forms
from .models import Update as UpdateModal

class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = UpdateModal
        fields =[
            'user',
            'content',
            'image'
        ]