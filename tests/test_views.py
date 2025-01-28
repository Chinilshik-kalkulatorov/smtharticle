# tests/test_views.py

import pytest
from django.urls import reverse
from blog.models import Article

@pytest.mark.django_db
def test_article_list_view(client):
    Article.objects.create(title="Test A")
    Article.objects.create(title="Test B")

    url = reverse('article_list')  # допустим, у вас name='article_list'
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode()
    assert "Test A" in content
    assert "Test B" in content