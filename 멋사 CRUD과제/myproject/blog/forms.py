from django import forms
from .models import Blog

class BlogUpdate(forms.ModelForm):
    class Meta:             #상위 클래스에 데이터를 담고 있는 클래스? 메타데이터
        model = Blog
        fields = ['title', 'body']