from django import forms
from .models import Post, Author, User
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
   #author = forms.CharField(initial=8, widget=forms.TextInput(attrs={'disabled': False}),label='автор')

   class Meta:
       model = Post
       fields = [
           'author',
           #'type',
           #'datetime_in', django.core.exceptions.FieldError: 'datetime_in' cannot be specified for Post model form as it is a non-editable field
           'head',
           'tekst',
           #'rating',
           'category',
       ]

   def clean(self):
       cleaned_data = super().clean()
       tekst = cleaned_data.get("tekst")
       if tekst is not None and len(tekst) < 20:
           raise ValidationError({
               "tekst": "Описание не может быть менее 20 символов."
           })

       head = cleaned_data.get("head")
       # tekst = cleaned_data.get("tekst")
       if head == tekst:
           raise ValidationError(
               # "текст статьи не должен совпадать с заголовком"
               {
                   "tekst": "текст новости не должен совпадать с заголовком"
               }
           )

       return cleaned_data


class ArtikullForm(forms.ModelForm):
   #type = forms.CharField(initial="AR", widget=forms.TextInput(attrs={'disabled': False} ) , label='вид') #widget=forms.HiddenInput(), required= False

   class Meta:
       model = Post
       fields = [
           'author',
           #'datetime_in', django.core.exceptions.FieldError: 'datetime_in' cannot be specified for Post model form as it is a non-editable field
           'head',
           'tekst',
           #'rating',
           'category',
       ]
       labels = {
           'author': 'Автор',
           'head': 'заголовок',
           'tekst': 'текст',
           'category': 'тема'
       }
       # widgets = {
       #     #'type': forms.HiddenInput(),
       #     #'type': forms.CharField(initial="AR"),
       #     'type': forms.TextInput(attrs={'disabled': True})
       # }

   def clean(self):
       cleaned_data = super().clean()
       tekst = cleaned_data.get("tekst")
       if tekst is not None and len(tekst) < 20:
           raise ValidationError({
               "tekst": "Описание не может быть менее 20 символов."
           })

       head = cleaned_data.get("head")
       # tekst = cleaned_data.get("tekst")
       if head == tekst:
           raise ValidationError(
               # "текст статьи не должен совпадать с заголовком"
               {
                   "tekst": "текст статьи не должен совпадать с заголовком"
               }
           )

       return cleaned_data