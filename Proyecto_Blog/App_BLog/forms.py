from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Article



class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(required=True,label = 'Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True,label = 'Repetir contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        
        
    

class UserEditForm(UserCreationForm):
    username = forms.CharField()
    usersurname = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir contraseña',widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ['username','usersurname','email','password1','password2']
        
        
   
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model= Article
        fields = ["title",'subtitle','description']
        
        
class AvatarForm(forms.Form):
    image = forms.ImageField()   
    