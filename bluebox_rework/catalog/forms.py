from django import forms
from users.models import Card

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Card
        widget = {
            'Card Number': forms.NumberInput(),
            'name': forms.CharField(),
            'lastName': forms.CharField(),

        }
        fields = ['cardNum', 'expirationDate', 'ccvNum']