import pytest
from api.clients.auth_client import AuthClient
from api.clients.product_client import ProductClient
from api.clients.cart_client import CartClient

BASE_URL = "http://www.example.com"

@pytest.fixture
def auth_cookies():
    auth_client = AuthClient(BASE_URL)
    return auth_client.login_stub()

@pytest.fixture
def product_id(auth_cookies):
    product_client = ProductClient(BASE_URL,auth_cookies)
    return product_client.create_product("Phone",50000)

@pytest.fixture
def cart_ready(auth_cookies,product_id):
    cart_client=CartClient(BASE_URL,auth_cookies)
    cart_client.add_item(product_id,quantity=1)

    