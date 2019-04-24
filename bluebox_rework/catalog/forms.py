from django import forms
from users.models import Users

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Users
        widget = {
            'CCVNumber': forms.NumberInput(),
        }
        fields = ['name', 'lastName', 'CCVNumber', 'expirationDate',]