import pytest


@pytest.mark.django_db
def test_index_view(client, profile, profile_index_url):
    response = client.get(profile_index_url)
    print(response)
    assert response.status_code == 200
    assert 'profiles/index.html' in [template.name for template in response.templates]
    assert profile.favorite_city == 'LA'


@pytest.mark.django_db
def test_profile_view(client, profile, profile_detail_url):
    response = client.get(profile_detail_url)
    assert response.status_code == 200
    assert 'profiles/profile.html' in [template.name for template in response.templates]
    assert profile.user.username == 'testuser'
    assert profile.user.last_name == 'Doe'
