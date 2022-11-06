from model_bakery import baker
# from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.test import APIClient
import pytest

from logistic.models import Stock, Product
# from stocks_products import settings


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def stocks_factory():
    def factory(*args, **kwargs):
        return baker.make(Stock, *args, **kwargs)
    return factory


@pytest.fixture
def products_factory():
    def factory(*args, **kwargs):
        return baker.make(Product, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(client, products_factory):
    # Arrange
    product = products_factory(_quantity=1)

    # Act
    response = client.get(f'/api/v1/products/{product[0].id}/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == product[0].title
