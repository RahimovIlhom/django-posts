from django import forms

from .models import Post, Comment, Reply


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body', 'tags']
        labels = {
            'body': 'Caption',
            'tags': 'Categories'
        }
        widgets = {
            'url': forms.TextInput(attrs={'placeholder': 'Add url ...'}),
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption ...', 'class': 'font1 text-4xl'}),
            'tags': forms.CheckboxSelectMultiple()
        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body': '',
            'tags': 'Categories'
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'}),
            'tags': forms.CheckboxSelectMultiple()
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add comment ...'})
        }
        labels = {
            'body': ''
        }


class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add reply ...', 'class': '!text-sm'})
        }
        labels = {
            'body': ''
        }
