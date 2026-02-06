import requests

class ProductClient:
    def __init__(self,base_url,auth_cookies):
        self.base_url = base_url
        self.auth_cookies = auth_cookies
    





    
    def create_product(self,name,price):
        payload = {
                "name" : name,
                "price":price
        }

        response = requests.post(f"{self.base_url}/products",
                                 json = payload,
                                 cookies = self.auth_cookies)
        
        response.raise_for_status()
        return response.json()["product_id"]