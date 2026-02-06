import requests

class CartClient:
    def __init__(self,base_url,auth_cookies):
        self.base_url = base_url
        self.auth_cookies = auth_cookies

    def add_item(self,product_id,quantity):
        payload = { 
            "product_id":product_id,
            "quantity":quantity
        }

        response = request.post(f"{base_url}/cart/items",
            json = payload,cookies = self.auth_cookies)
        
        response.raise_for_status()

    