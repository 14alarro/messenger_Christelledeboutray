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
    def create_channel(self,nom):
        requests.post(f"{self.url}/channels/create",json={"name": nom} )
    def get_channels(self):
        reponse=requests.get(f"{self.url}/channels")
        L=reponse.json()
        L_channels=[]
        for channel in L:
            L_channels.append(channel["name"])
        return L_channels
    def add_channel(self,nom):
        requests.post(f"{self.url}/channels/create",json={"name": nom} )
    def get_messages(self):
        reponse=requests.get(f"{self.url}/messages")
        L=reponse.json()
        L_messages=[]
        for message in L:
            L_messages.append(message["content"])
        return  L_messages
    def get_channel_id(self,channel):
        reponse=requests.get(f"{self.url}/channels")
        L=reponse.json()
        i=0
        n=len(L)
        while i<n and L[i]['name']!=channel:
            i+=1
        if i==n:
            print("groupe inexistant")
            channel=input("donner moi un groupe qui existe")
            self.get_channel_id(channel)
        else:
            channel_id=L[i]['id']
        return(L[i]['id'])
    def get_user_id(self,user):
        reponse=requests.get(f"{self.url}/users")
        L=reponse.json()
        i=0
        n=len(L)
        while i<n and L[i]['name']!=user:
            i+=1
        if i==n:
            print("utilisateur inexistant")
            user=input("donner moi un utilisateur qui existe")
            self.get_user_id(user)
        else:
            user_id=L[i]['id']
        return(user_id)
    def join_group(self,channel,user):
        channel_id=self.get_channel_id(channel)
        user_id=self.get_user_id(user)
        requests.post(f"{self.url}/channels/{channel_id}/join",json={"user_id": user_id} )
    def see_members_group(channel,self):
        channel_id=self.get_channel_id(channel)
        reponse=requests.get(f"{self.url}/channels/{channel_id}/members").json()
        L=[]
        for user in reponse:
            L.append(user['name'])
        print(L)
    def post_messages(self, channel, content, sender):
        channel_id=self.get_channel_id(channel)
        sender_id=self.get_user_id(sender)
        requests.post(f"{self.url}/{channel_id}/messages/post",json={"sender_id": sender_id, "content": content} )




