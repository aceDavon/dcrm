from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Sign_Up_Form(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-full rounded-md p-2 border', 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-full rounded-md p-2 border', 'placeholder': 'Enter Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'w-full rounded-md p-2 border', 'placeholder': 'Enter Email address'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1')

    def __init__(self, *args, **kwargs):
        super(Sign_Up_Form, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'w-full rounded-md p-2 border'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter a username'
        self.fields['username'].help_text = ""

        self.fields['password1'].widget.attrs['class'] = 'w-full rounded-md p-2 border'
        self.fields['password1'].widget.attrs['placeholder'] = ''
        self.fields['password1'].help_text = "<ul class='flex flex-col  space-y-2 items-center p-2'><li class='text-xs text-red-500 italic whitespace-normal text-left w-96'>Password Must be 6 characters long</li><li class='text-xs text-red-500 italic whitespace-normal  text-left w-96'>Password Must contain numbers, alphabets and symbols and can also be a combination of upper and lower case letters</li><li class='text-xs text-red-500 italic whitespace-normal text-left w-96'>Password Must not contain text similar to the other data provided</li></ul>"

        self.fields['password2'].widget.attrs['class'] = 'w-full rounded-md p-2 border'
        self.fields['password2'].widget.attrs['placeholder'] = ''
        self.fields['password2'].help_text = ""
