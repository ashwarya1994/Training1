from django import forms
from appTwo.models import User

class NewUser(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget =forms.Textarea)
    class Meta():
        model = User
        fields = 'first_name', 'last_name', 'email'
