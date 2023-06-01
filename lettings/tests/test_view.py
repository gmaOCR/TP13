import pytest


@pytest.mark.django_db
def test_index_view(client, letting, letting_index_url):
    response = client.get(letting_index_url)
    assert response.status_code == 200
    assert 'lettings/index.html' in [template.name for template in response.templates]
    assert letting.title in response.content.decode()


@pytest.mark.django_db
def test_letting_view(client, letting, letting_detail_url):
    response = client.get(letting_detail_url)
    assert response.status_code == 200
    assert 'lettings/letting.html' in [template.name for template in response.templates]
    assert letting.title in response.content.decode()
    assert letting.address in response.content.decode()
