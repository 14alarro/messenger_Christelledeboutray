# il faut que l'on ait une fonction remote server ici 
# il faut faire un request.post 

import requests
import json
from model import User

class RemoteServer:
    def __init__(self,url):
        self.url=url
    def get_users(self):
        reponse=requests.get(f"{self.url}/users")
        L=reponse.json()
        L_users=[]
        for user in L:
            L_users.append(user["name"])
        return  L_users
    def add_users(self,nom):
        requests.post(f"{self.url}/users/create",json={"name": nom} )
    def get_channels(self):
        reponse=requests.get(f"{self.url}/channels")
        L=reponse.json()
        L_channels=[]
        for channel in L:
            L_channels.append(channel["name"])
    def add_channel(self):
        requests.post(f"{self.url}/channels/create",json={"name": nom} )
    def get_messages(self):
        reponse=requests.get(f"{self.url}/messages")
        L=reponse.json()
        L_messages=[]
        for message in L:
            L_messages.append(message["content"])
        return  L_messages
    def join_group(self,channel_id,user_id):
        requests.post(f"{self.url}/{channel_id}/create",json={"user_id": user_id} )
    def post_messages(self, channel_id, content, sender_id):
        requests.post(f"{self.url}/{channel_id}/messages/post",json={"sender_id": sender_id, "content": content} )



#modifier les fonctions de manière à avoir les noms des groupes que l'on manipule
#utiliser notion override et héritage
# que fait @abstractmethod: documentation

#server contient toutes les méthodes avec des pass
#si on n'a pas une version de python qui est assez avancé pour mettre override, on ne va rien mettre

    


#response=requests.get("https://groupe5-python-mines.fr/users")
#print(response.json())

