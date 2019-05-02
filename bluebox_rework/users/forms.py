from django import forms
from users.models import Users, Card

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        widget = {
            'email': forms.EmailField(),
            'password': forms.PasswordInput(),
        }
        body = forms.CharField(widget=forms.Textarea)
        fields = ['name', 'lastName', 'email', 'password', 'DOB', 'userName',]

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Card
        widget = {
            'cardNum': forms.IntegerField(),
            'expirationDate': forms.DateInput(),
            'ccvNum': forms.IntegerField(),

        }
        fields = ['cardNum', 'expirationDate', 'ccvNum',]

class LoginForm(forms.ModelForm):
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