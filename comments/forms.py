from django import forms
from . import models


class CommentModelForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = [
            'name',
            'email',
            'comment',
            'post',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }
        labels = {
            'name': 'Seu Nome:',
            'email': 'E-mail:',
            'comment': 'Comentário'
        }
