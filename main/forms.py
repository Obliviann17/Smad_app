from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        else:
            return user


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", 'last_name', 'email', 'address', 'phone_number', 'city', 'card_number', 'cvv_code', 'validity']