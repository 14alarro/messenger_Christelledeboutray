import json 
from model import Message, Channel,User

# faire ça partout

class LocalServer:
    def __init__(self,LocalServer_FILE_NAME):
        with open(LocalServer_FILE_NAME) as f:
            LocalServer=json.load(f)
            L_messages=[]
            for message in LocalServer['messages']:
                id=message['id']
                reception_date=message['reception_date']
                sender_id = message['sender_id']
                channel=message['channel']
                content=message['content']
                element = Message(id, reception_date, sender_id, channel, content)
                L_messages.append(element)
            L_channels=[]
            for channel in LocalServer['channels']:
                id=channel['id']
                name=channel['name']
                member_ids=channel['member_ids']
                element=Channel(id,member_ids,name)
                L_channels.append(element)
            L_users=[]
            for user in LocalServer['users']:
                id=user['id']
                name=user['name']
                element = User(id, name)
                L_users.append(element)
            self.users=L_users
            self.channels=L_channels
            self.messages=L_messages
    def __repr__(self):
        return(f"LocalServer(users={self.users},channels={self.channels}, messages={self.messages}")
    def save(self):
        # fonction qui passe d'une classe à un dictionnaire afin de faire le json.dump
        serveur={}
        #LocalServer.users contient une somme d'objets 
        L_users=[user.to_dict() for user in self.users]
        serveur['users']=L_users
        L_channels=[channel.to_dict() for channel in self.channels]
        serveur["channels"]=L_channels
        L_messages=[message.to_dict() for message in self.messages]
        serveur["messages"]=L_messages
        with open('LocalServer.json', 'w') as f:
            json.dump(serveur, f,indent=10) 
    def get_users(self):
        L_users=[]
        for user in self.users:
            L_users.append(user.name)
        return ("la liste est",L_users)
    def get_messages(self):
        L_messages=[message.to_dict() for message in self.messages]
        return (L_messages)
    def get_channels(self):
        L_channels=[channel.to_dict() for channel in self.channels]
        print(L_channels)

