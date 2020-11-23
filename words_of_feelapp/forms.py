from django import forms
from .models import Registration
from .models import Quotes

class RegistrationFrom(forms.ModelForm):
    class Meta:
        model=Registration
        fields=['user_first_name','user_last_name','user_email','user_password','user_mobile']
        widgets = {
        'user_password': forms.PasswordInput()
         }


class QuotesFrom(forms.ModelForm):
    class Meta:
        model=Quotes
        #model=Registration
        fields=['Quote_image','Quote_caption']

class LoginFrom(forms.ModelForm):
    class Meta:
        model=Registration
        fields=['user_email','user_password']
        widgets = {
        'user_password': forms.PasswordInput()
         }

class forgotpasswordform(forms.ModelForm):
    class Meta:
        model=Registration
        fields=['user_email','user_mobile']