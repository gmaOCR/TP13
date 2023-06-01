import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


@pytest.fixture
def profile():
    user = User.objects.create(username='testuser', first_name='John', last_name='Doe')
    return Profile.objects.create(user=user, favorite_city='LA')


@pytest.fixture
def profile_index_url():
    return reverse('profiles:profiles_index')


@pytest.fixture
def profile_detail_url(profile):
    return reverse('profiles:profile', kwargs={'username': profile.user.username})
