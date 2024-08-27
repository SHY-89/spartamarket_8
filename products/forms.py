from django import forms
from .models import Product, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("uuid", "like_users", "cnt", "hashtags", )
        labels = {
            "title": "제목",
            "content": "설명",
            
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목'}),
            'content': forms.Textarea(attrs={'placeholder': '게시글 내용을 작성해 주세요.'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text'] 
        exclude = ("product",)  
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 2,  # 세로
                'cols': 40,  # 가로
                'style': 'resize:none;',  # 사용자 제한
                'placeholder': '댓글을 입력하세요.'  
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
            'class': 'custom-comment-textarea',
        })