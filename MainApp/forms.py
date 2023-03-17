from MainApp.models import Snippet, Languages
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Snippets.settings import choices
class SnippetForm(forms.ModelForm):
    class Meta:
      model = Snippet
      # Описываем поля, которые будем заполнять в форме
      fields = ['name', 'language', 'code','public']

      widgets = {
          'name': forms.TextInput(attrs={"class":"form-control form-control-lg", 'placeholder': 'Название сниппета'}),
          'language': forms.Select(attrs={"class": "form-control form-control-lg", 'placeholder': 'Язык'}, choices=choices),
          'code': forms.Textarea(attrs={"class": "form-control form-control-lg", 'placeholder': 'Название сниппета', 'cols': '96', 'rows': '10'}),
          'public': forms.CheckboxInput(attrs={"class": "form-check-input"})
      }
      labels = {
          'name': ''
      }


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


