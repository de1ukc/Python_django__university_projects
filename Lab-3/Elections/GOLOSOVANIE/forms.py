from django import forms
from .models import Candidate, Batch

# class CandidateForm(forms.Form):
#     first_name = forms.CharField(max_length=150, label='Имя', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#         }
#     ))
#
#     last_name = forms.CharField(max_length=150, label='Фамилия', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#         }
#     ))
#
#     middle_name = forms.CharField(max_length=150, label='Отчество', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#         }
#     ))
#
#     date_of_birth = forms.DateField(label='Дата рождения', widget=forms.DateInput(
#             attrs={
#                 'class': 'date',
#                 'placeholder': 'D.M.YYYY',
#             }))  # ????? как-то плохо вышло
#
#     region = forms.CharField(max_length=150, label='Регион', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#         }
#     ))
#
#     description = forms.CharField(label='Описание', widget=forms.Textarea(
#         attrs={
#             'class': 'form-control',
#             'rows': 5,
#         }
#     ))
#
#     slogan = forms.CharField(max_length=100, label='Слоган', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#         }
#     ))
#
#     batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=False, empty_label='Самовыдвиженец',
#                                    label='Партия', widget=forms.Select(
#             attrs={
#                 'class': 'form-control',
#             }
#         ))
#
#     preview = forms.ImageField(label='Фотокарточка')


class CandidateForm(forms.ModelForm):

    # slogan2 = forms.CharField(max_length=100, label='Слоган', widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #     }
    # ))
    #

    class Meta:
        model = Candidate

        fields = ['first_name', 'last_name', 'middle_name', 'date_of_birth', 'region', 'description',
                  'batch', 'preview', 'slogan']

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

            'slogan': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'batch': forms.Select(attrs={
                'class': 'form-control',
            })
        }
