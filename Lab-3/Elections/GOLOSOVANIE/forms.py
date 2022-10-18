from django import forms
from .models import Candidate, Batch, StartPage, MyUser, Slogan
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate

        fields = ['first_name', 'last_name', 'middle_name', 'date_of_birth', 'region', 'description',
                  'batch', 'preview', 'slogan', 'creator']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'middle_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'date_of_birth': forms.DateInput(attrs={
                'class': 'date',
                'placeholder': 'D.M.YYYY',
            }),

            'region': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '5',
            }),

            'slogan': forms.Select(attrs={
                'class': 'form-control',
            }),

            'batch': forms.Select(attrs={
                'class': 'form-control',
            }),

            'creator': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class CreateBatchForm(forms.ModelForm):
    class Meta:
        model = Batch

        fields = ['name', 'political_views']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'political_views': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }


class SloganForm(forms.ModelForm):
    class Meta:
        model = Slogan

        fields = ('slogan',)

        widgets = {
            'slogan': forms.TextInput(attrs={
                'class': 'form-control',
            })
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }
    ))

    username = forms.CharField(max_length=30, label='Имя пользователя', help_text="Имя должно быть на английском",
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                   }
                               ))

    nick_name = forms.CharField(max_length=30, label='Ник', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    password1 = forms.CharField(max_length=30, label='Пароль', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))

    password2 = forms.CharField(max_length=30, label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = MyUser
        fields = ('username', 'nick_name', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, label='Имя пользователя', help_text="Имя должно быть на английском",
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                   }
                               ))

    password = forms.CharField(max_length=30, label='Пароль', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
