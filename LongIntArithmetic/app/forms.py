from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LongIntForm(forms.Form):

    number1 = forms.CharField(max_length=100)
    number2 = forms.CharField(max_length=100)

    def clean_number1(self):
        """
        Validate number1 field. Check if the string contains only digits
        :return: The cleaned data
        """
        data = self.cleaned_data['number1']
        if not data.isdigit():
            raise ValidationError(_('Invalid number'), code='invalid')
        return data

    def clean_number2(self):
        """
        Validate number2 field. Check if the string contains only digits
        :return: The cleaned data
        """
        data = self.cleaned_data['number2']

        if not data.isdigit():
            raise ValidationError(_('Invalid number'), code='invalid')

        return data