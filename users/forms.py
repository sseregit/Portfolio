from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.contrib.auth.models import User
from django import forms


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label='이메일 주소',required=True, widget=forms.EmailInput(attrs={'placeholder': '이메일 주소'}))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


