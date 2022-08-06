from django import forms
from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='enter your name:', max_length=20, min_length=1)
    last_name = forms.CharField(label='enter your last name:', max_length=20, min_length=1)
    username = forms.CharField(label='enter your username:', max_length=20)
    password = forms.CharField(label='enter password', max_length=20, widget=forms.PasswordInput(), validators=[
        MinLengthValidator(limit_value=7, message="password too short")
    ])
    confirm_password = forms.CharField(label='renter password', max_length=20, widget=forms.PasswordInput(),
                                       validators=[
                                           MinLengthValidator(limit_value=7, message="password too short")
                                       ])
    email = forms.EmailField(max_length=30)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "plz select another username"
            )
        return username


