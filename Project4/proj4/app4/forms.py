from django import forms
from . models import signup,gallery

class RegisterForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    Date = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'type': 'date'}), )
    class Meta():
        model = signup
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta():
        model = signup
        fields = ('Email','Password',)

class EditForm(forms.ModelForm):
    class Meta():
        model = signup
        fields = ('Name','Password','Email',)

class GalleryForm(forms.ModelForm):
    class Meta():
        model = gallery
        fields = '__all__'