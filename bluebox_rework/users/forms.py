from django import forms
from users.models import Users

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        widget = {
            'password': forms.PasswordInput(),
            'CCVNumber': forms.NumberInput(),
        }
        body = forms.CharField(widget=forms.Textarea)
        fields = '__all__'
