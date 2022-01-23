from django.db import models

# Create your models here.
from django.utils import timezone  # django で日付を管理するためのモジュール
from markdownx.models import MarkdownxField

from django.utils.safestring import mark_safe
from markdownx.utils import markdownify


class Post(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = MarkdownxField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

    def get_text_markdownx(self):
        return mark_safe(markdownify(self.text))

    def __str__(self):  # Post モデルが直接呼び出された時に返す値を定義
        return self.title  # 記事タイトルを返す
