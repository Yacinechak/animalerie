from django import forms
 
from .models import Animal
 
class MoveForm(forms.ModelForm):
 
    class Meta:
        model = Animal
        fields = ('lieu',)