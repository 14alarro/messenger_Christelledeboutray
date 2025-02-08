import json 
from model import Message, Channel,User
from datetime import datetime




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

    def create_channel(self,nom):
        id=max([channel.id for channel in self.channels])+1
        new_user=User(id,nom)
        self.channels.append(new_user)
        self.save()

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

    def get_user_name(self,id):
        L_users=self.users
        n=len(L_users)
        while i<n and L_users[i].id!=id:
            i+=1
        if i==n:
            print("cette personne n'existe pas")
            id=input("donne moi une personne qui existe")
            self.get_users_name(self,id) 
        return(L_users[i].name)
    def get_user_id(self,user):
        L_users=self.users
        n=len(L_users)
        while i<n and L_users[i].name!=user:
                i+=1
        if i==n:
                print("cette personne n'existe pas")
                user=input("donne moi une personne qui existe")
                self.get_users_id(self,user)
        return(L_users[i].id)
    def get_channel_id(self,channel):
        L_channels=self.channels
        n=len(L_channels)
        while i<n and L_channels[i].name!=channel :
                i+=1
        if i==n:
                print("ce groupe n'existe pas")
                channel=input("donne moi un groupe qui existe")
                self.get_users_id(self,channel)
        return(L_channels[i].id)
    def get_users(self):
        L_users=[]
        for user in self.users:
            L_users.append(user.name)
        return (L_users)
    def get_messages(self):
        L_messages=[message.to_dict() for message in self.messages]
        return (L_messages)
    def get_channels(self):
        L_channels=[channel.to_dict() for channel in self.channels]
        print(L_channels)
    def see_members_group(channel,self):
        L_channels=self.channels
        j=0
        n=len(L_channels)
        while j<n and L_channels[j].name!=channel:
            j+=1
        if j==n:
            print("ce groupe n'existe pas")
            channel=input("donner moi un groupe qui existe")
            self.see_members_group(channel)
        else:
            L_ids=L_channels[j].member_ids
            L_names=[]
            for id in L_ids:
                L_names.append(self.get_user_name(id))
            print(L_names)

            
    def join_group(self,channel,user):
        member_id=self.get_user_id(user)  
        j=0
        L_channels=self.channels
        while L_channels[j].name!=channel:
            j=j+1
        if j==(len(L_channels)+1):
            print("ce groupe n'existe pas")
        else:
            L_channels[j].member_ids.append(member_id)
            self.channels=L_channels
        self.save()

    def post_messages(self, channel, content, sender):
         channel_id=self.get_channel_id(channel)
         sender_id=self.get_user_id(sender)
         reception_date=str(datetime.now())
         id = max([message.id for message in self.messages])+1
         new_message=Message(self,id,reception_date,sender_id, channel_id,content)
         L_messages=self.messages
         L_messages.append(new_message)
         self.messages=L_messages
         self.save()
        
