from django import forms
from rango.models import Page, Category
from django.contrib.auth.models import User
from rango.models import UsersProfile

class CategoryForm(forms.ModelForm):
    
    name = forms.CharField(max_length=128,help_text="Please enter the category names.")
    
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    
    likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    
    slug = forms.CharField(widget=forms.HiddenInput, required=False)
    
    
    class Meta:
        model = Category
        fields = ('name',)
        
        
        
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,help_text="Please enter the title names.")
    
    url = forms.URLField(max_length=200, help_text="please enter URL")
    
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    
    
    class Meta:
        model = Page
        exclude = ('category',)
        
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UsersProfile
        fields = ('website', 'picture')
        
        
        
        
    
    
    
    