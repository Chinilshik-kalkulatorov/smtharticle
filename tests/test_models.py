# tests/test_models.py

import pytest
from django.db import IntegrityError
from blog.models import Article

@pytest.mark.django_db
def test_create_article():
    # Проверим, что можем создать Article (title, exe_file и т.д.)
    article = Article.objects.create(title="My first article")
    assert article.id is not None
    assert article.title == "My first article"

@pytest.mark.django_db
def test_article_title_required():
    # Проверим, что если title обязательное поле, при отсутствии вылетит ошибка
    with pytest.raises(IntegrityError):
        Article.objects.create(title=None)