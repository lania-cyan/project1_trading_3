from django import forms
from joonggo.models import Sell, Comment

class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ['subject', 'content']
        lables = {
            'subject': '제목',
            'content': '내용',
        }

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows':10}),
        }

        lables = {
            'subject': '제목',
            'content': '내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
        'content': '답변내용',
        }