from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','title_tag','author','Category','tags','body','snippet','image','draft','publish']

        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "title_tag": forms.TextInput(attrs={'class': 'form-control'}),
            "author": forms.TextInput(attrs={'class': 'form-control','value':' ','type':'hidden'}),
            "Category": forms.Select(attrs={'class': 'form-control'}),
            "body": forms.Textarea(attrs={'class': 'form-control'}),
            "snippet": forms.Textarea(attrs={'class': 'form-control'}),
            "publish": forms.TextInput(attrs={'class':'form-control'}),
            "tags": forms.TextInput(attrs={'class': 'form-control'})
        }

class updateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','title_tag','body','snippet','image','draft','publish']

        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "title_tag": forms.TextInput(attrs={'class': 'form-control'}),
            "body": forms.Textarea(attrs={'class': 'form-control'}),
            "snippet": forms.Textarea(attrs={'class': 'form-control'}),
            "publish": forms.TextInput(attrs={'class': 'form-control'}),
            "tags": forms.TextInput(attrs={'class': 'form-control'})
        }