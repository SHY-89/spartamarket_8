from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ('uuid', 'like_users')
        labels = {
            "title": "제목",
            "content": "설명",
            
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목'}),
            'content': forms.Textarea(attrs={'placeholder': '게시글 내용을 작성해 주세요.'}),
        }
        
