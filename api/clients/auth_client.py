import requests

class AuthClient:
    def __init__(self,base_url):
        self.base_url = base_url

    def login_stub(self):
        """Assumes authentication is successful"""   
        return {"session":"fake session cookie"}


    def login_real(self,username,password):
        
        """
        Real authentication using HTTP API.
        Can be enabled when a live environment is available.
        """


        payload = { 
                "username" : username,
                "password" : password
            
                }

        response  = requests.post(f"{self.base_url}/login",json=payload)
        response.raise_for_status()
        return response.cookies 
    
    
    
