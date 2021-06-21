from django import forms
from .models import Post

from markdownx.widgets import MarkdownxWidget


class PostCreateForm(forms.ModelForm):  # DjangoのModelFormでは強力なValidationを使える

    class Meta:
        model = Post  # Post モデルと接続し、Post モデルの内容に応じてformを作ってくれる
        fields = ('title', 'text')  # 入力するカラムを指定
        widgets = {
            'text': MarkdownxWidget(),
        }
