from django import forms
from users.models import Users

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        widget = {
            'email': forms.EmailField(),
            'password': forms.PasswordInput(),
            'CCVNumber': forms.NumberInput(),
        }
        body = forms.CharField(widget=forms.Textarea)
        fields = '__all__'

class LogixnForm(forms.ModelForm):
    class Meta:
        model = Users
        widget = {
            'password': forms.PasswordInput(),
        }
        fields = ['userName', 'password',]

class ForgotForm(forms.ModelForm):
    class Meta:
        model = Users
        widget = {
            'email': forms.EmailField(),
        }
        fields = ['email',]