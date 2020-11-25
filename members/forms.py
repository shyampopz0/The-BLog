from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

        # widgets = {
        #     "username":forms.TextInput(attrs={'class':'form-control'}),
        #     "password1":forms.PasswordInput(attrs={'class':'form-control'}),
        #     "password2": forms.PasswordInput(attrs={'class': 'form-control'})
        # }

    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        #self.fields['password1'].help_text = ''

class updateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','facebook_url','twitter_url','instagram_url')

        widgets = {
            "user":forms.TextInput(attrs={'class':'form-control'}),
            "bio":forms.Textarea(attrs={'class':'form-control'}),
            "facebook_url":forms.TextInput(attrs={'class':'form-control'}),
            "twitter_url":forms.TextInput(attrs={'class':'form-control'}),
            "instagram_url":forms.TextInput(attrs={'class':'form-control'})
        }