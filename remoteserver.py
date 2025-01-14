# il faut que l'on ait une fonction remote server ici 
# il faut faire un request.post 

import requests
import json


class RemoteServer:
    def __init__(self,url):
        self.server=requests.get(url)
        self.url=url
    def get_users(self):
        response=self.server.json()
        L_users=[]
        for user in response:
            L_users.append(user["name"])
        return  L_users
    def create_users(self):
        #resquest.post )
    
