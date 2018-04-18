from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    """ 文章表单 """
    class Meta:
        """docstring for Meta"""
        model = Article
        fields = ['title', 'body','category']
        TextInput = {'title': ''}
        Textarea = {'body': ''}
        ChoiceField = {'category': ''}

        
class NewArticleForm(forms.ModelForm):
    """  新建文章表单 """
    class Meta:
        model = Article
        fields = ['title', 'body', 'category', 'author']
        TextInput = {'title': '', 'author': ''}
        Textarea = {'body': ''}
        ChoiceField = {'category': ''}
