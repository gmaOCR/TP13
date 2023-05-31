import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Letting, Address


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def address():
    return Address.objects.create(number=123, street='Test Street', city='Test City', state='TS',
                                  zip_code=12345, country_iso_code='TST')


@pytest.fixture
def letting(address):
    return Letting.objects.create(title='Test Letting', address=address)


@pytest.fixture
def letting_index_url():
    return reverse('lettings:index')


@pytest.fixture
def letting_detail_url(letting):
    return reverse('lettings:letting', kwargs={'letting_id': letting.id})
