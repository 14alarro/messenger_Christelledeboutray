import requests
import json
from model import Channel, Message, User

class RemoteServer:
    def __init__(self,url: str):
        self.url=url

    # Il vaut mieux créer des objets `User` le plus tôt possible,
    # et les renvoyer pour donner accès aux `id` comme aux `name`.
    # Comme la signature de la fonction (les types des paramètres
    # et de la valeur de retour) est la même que pour
    # `LocalServer.get_users`, vous pouvez utiliser ces 2 fonctions
    # de la même façon.
    def get_users(self) -> 'list[User]':
        reponse=requests.get(f"{self.url}/users")
        # Evitez d'utiliser des noms de variables d'une seule
        # lettre, il vaut mieux être explicite.
        # Même si votre fonction est simple aujourd'hui, elle pourrait
        # se complexifier à l'avenir.
        users_as_dicts = reponse.json()
        return [User.from_dict(user_as_dict) for user_as_dict in users_as_dicts]

    def add_user(self,nom: str) -> None:
        requests.post(f"{self.url}/users/create",json={"name": nom} )
    def create_channel(self,nom: str) -> None:
        requests.post(f"{self.url}/channels/create",json={"name": nom} )

    def get_channels(self) -> 'list[Channel]':
        reponse=requests.get(f"{self.url}/channels")
        channels_as_dicts = reponse.json()
        return [Channel.from_dict(channel_as_dict) for channel_as_dict in channels_as_dicts]

    def add_channel(self,nom: str) -> None:
        requests.post(f"{self.url}/channels/create",json={"name": nom} )

    def get_messages(self) -> 'list[Message]':
        reponse=requests.get(f"{self.url}/messages")
        messages_as_dicts = reponse.json()
        return [Message.from_dict(message_as_dict) for message_as_dict in messages_as_dicts]

    def get_channel_id(self, channel_name: str) -> int:
        reponse=requests.get(f"{self.url}/channels")
        L=reponse.json()
        i=0
        n=len(L)
        while i<n and L[i]['name']!=channel_name:
            i+=1
        if i==n:
            print("groupe inexistant")
            channel_name=input("donner moi un groupe qui existe")
            return self.get_channel_id(channel_name)

        return(L[i]['id'])

    def get_user_id(self,user_name: str) -> int:
        reponse=requests.get(f"{self.url}/users")
        L=reponse.json()
        i=0
        n=len(L)
        while i<n and L[i]['name']!=user_name:
            i+=1
        if i==n:
            print("utilisateur inexistant")
            user_name=input("donner moi un utilisateur qui existe")
            return self.get_user_id(user_name)
        else:
            user_id=L[i]['id']
        return(user_id)

    def join_group(self, channel_name: str, user_name: str) -> None:
        channel_id=self.get_channel_id(channel_name)
        user_id=self.get_user_id(user_name)
        requests.post(f"{self.url}/channels/{channel_id}/join",json={"user_id": user_id} )

    def see_members_group(self, channel) -> 'list[str]':
        channel_id=self.get_channel_id(channel)
        reponse=requests.get(f"{self.url}/channels/{channel_id}/members").json()
        L=[]
        for user in reponse:
            L.append(user['name'])
        return L

    def post_messages(self, channel: str, content: str, sender: str) -> None:
        channel_id=self.get_channel_id(channel)
        sender_id=self.get_user_id(sender)
        requests.post(f"{self.url}/{channel_id}/messages/post",json={"sender_id": sender_id, "content": content} )
