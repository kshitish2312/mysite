from django import forms
from django.contrib.auth.models import User
from  .models import Post, Comment
from datetime import date
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PostForm(forms.ModelForm):
    #published_date = forms.DateTimeField(widget=forms.SelectDateWidget,initial=timezone.now())
    #published_date = forms.DateTimeField(widget=forms.SelectDateWidget(initial=timezone.input))
    class Meta:
        model = Post
        fields = ('title','text')



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Sign up','Sign up', css_class='btn-primary'))
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
