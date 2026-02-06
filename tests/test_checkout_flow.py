from api.clients.order_client import OrderClient
from ui.pages.checkout_page import CheckoutPage


base_url = "http://example.com"

def test_user_can_checkout_product(cart_ready,auth_cookies,driver): 

    # checkout_page.open()  
    checkout_page = CheckoutPage(driver)
    checkout_page.complete_checkout()
    
    order_client = OrderClient(base_url,auth_cookies)
    order_id = order_client.place_order()

    order = order_client.get_order(order_id)
    assert order["status"] == "CREATED"