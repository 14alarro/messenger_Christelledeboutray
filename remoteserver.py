# il faut que l'on ait une fonction remote server ici 
# il faut faire un request.post 

import requests
import json


class RemoteServer:
    def __init__(self,url):
        self.url=url
    def get_users(self):
        print("on lance la fonction get users")
        reponse=requests.get(self.url)
        L=reponse.json()
        L_users=[]
        for user in L:
            L_users.append(user["name"])
        return  L_users
    def add_users(self,nom):
        print("je voulais ajouter un utilisateur")
        requests.post(f"{self.url}/create",json={"name": nom} )
    


response=requests.get("https://groupe5-python-mines.fr/users")
print(response.json())