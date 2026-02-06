class OrderClient:
    def __init__(self,base_url,auth_cookies):
        self.base_url = base_url 
        self.auth_cookies = auth_cookies 

    def place_order(self):
        response = requests.post(f"{self.base_url}/orders",
                                 cookies = self.auth_cookies
        )
        response.raise_for_status()
        return response.json()["order_id"]
    
    def get_order(self,order_id):
        response = requests.get(f"{self.base_url}/orders/{order_id}",
                                cookies=self.auth_cookies)
        response.raise_for_status()
        return response.json()