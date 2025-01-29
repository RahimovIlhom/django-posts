from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        labels = {
            'realname': 'Name'
        }
        widgets = {
            'image': forms.FileInput(),
            'bio': forms.Textarea(attrs={'rows': 3})
        }

