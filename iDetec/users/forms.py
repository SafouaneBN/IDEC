from django.forms import forms

from .models import User


class formUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'