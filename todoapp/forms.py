from .models import mytask
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=mytask
        fields=['name','priority','date']
