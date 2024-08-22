from django import forms
from .models import Index

class ProductForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = "__all__"
        labels = {
            "title": "제목",
            "content": "내용",
            
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목'}),
            'content': forms.Textarea(attrs={'placeholder': '내용'}),
        }
        
