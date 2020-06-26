from django import forms
from .models import Post, Blog


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"