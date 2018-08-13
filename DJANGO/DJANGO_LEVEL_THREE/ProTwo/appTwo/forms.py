from django import forms
from appTwo.models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
