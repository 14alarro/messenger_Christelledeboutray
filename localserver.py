import json 
from model import Message, Channel,User
from datetime import datetime




class LocalServer:
    # N'oubliez pas d'indiquer le type des arguments dans vos fonctions
    def __init__(self,LocalServer_FILE_NAME: str):
        # Vous pouvez stocker le nom du fichier afin d'y
        # avoir accès dans la fonction `save`
        self.storage_file_name = LocalServer_FILE_NAME
        with open(LocalServer_FILE_NAME) as f:
            LocalServer=json.load(f)
            # Vous n'avez pas besoin de créer une
            # liste intermédiaire, vous pouvez directement
            # travailler sur la liste `self.messages`
            self.messages: 'list[Message]' = []
            for message_as_dict in LocalServer['messages']:
                # Votre code fonctionnait bien. Une alternative
                # est d'utiliser une fonction `from_dict`,
                # qui permet de simplifier la lecture de votre code.
                message = Message.from_dict(message_as_dict)
                self.messages.append(message)
            self.channels: 'list[Channel]' = []
            for channel_as_dict in LocalServer['channels']:
                channel = Channel.from_dict(channel_as_dict)
                self.channels.append(channel)
            self.users: 'list[User]' = []
            for user_as_dict in LocalServer['users']:
                user = User.from_dict(user_as_dict)
                self.users.append(user)

    def create_channel(self,nom: str) -> None:
        id=max([channel.id for channel in self.channels])+1
        new_channel = Channel(id, [], nom)
        self.channels.append(new_channel)
        self.save()

    def __repr__(self) -> str:
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
        with open(self.storage_file_name, 'w') as f:
            json.dump(serveur, f,indent=10)

    def get_user_name(self,id: int) -> str:
        L_users=self.users
        n=len(L_users)
        i = 0 # N'oubliez pas d'initialiser vos variables
              # avant de les utiliser
        while i<n and L_users[i].id!=id:
            i+=1
        if i==n:
            print("cette personne n'existe pas")
            id=int(input("donne moi une personne qui existe"))
            return self.get_user_name(id) # Le paramètre `self` est passé automatiquement
        return L_users[i].name

    # N'hésitez pas à utiliser des noms de variables plus long
    # mais plus explicites : le mot `user` peut désigner un objet
    # de type `User`, un dictionnaire, un nom...
    def get_user_id(self, user_name: str) -> int:
        L_users=self.users
        n=len(L_users)
        i = 0
        while i<n and L_users[i].name!=user_name:
                i+=1
        if i==n:
                print("cette personne n'existe pas")
                user_name=input("donne moi une personne qui existe")
                return self.get_user_id(user_name)
        return(L_users[i].id)
    
    def get_channel_id(self,channel_name: str) -> int:
        L_channels=self.channels
        n=len(L_channels)
        i = 0
        while i<n and L_channels[i].name!=channel_name :
                i+=1
        if i==n:
                print("ce groupe n'existe pas")
                channel_name = input("donne moi un groupe qui existe")
                return self.get_channel_id(channel_name)
        return(L_channels[i].id)

    def get_users(self) -> 'list[User]':
        # Pas besoin de créer une nouvelle liste
        return self.users
    def get_messages(self) -> 'list[Message]':
        return self.messages
    def get_channels(self) -> 'list[Channel]':
        return self.channels

    # J'ai récupéré cette fonction dans votre fichier server.py
    def add_user(self, nom: str) -> None:
        id=max([user.id for user in self.users])+1

        new_user=User(id, nom)
        self.users.append(new_user)
        self.save()

    # `self` doit toujours être le premier paramètre,
    # comme `cls` pour une `classmethod`
    def see_members_group(self, channel_name: str) -> 'list[str]':
        L_channels=self.channels
        j=0
        n=len(L_channels)
        while j<n and L_channels[j].name!=channel_name:
            j+=1
        if j==n:
            print("ce groupe n'existe pas")
            channel_name=input("donner moi un groupe qui existe")
            return self.see_members_group(channel_name)
        else:
            L_ids=L_channels[j].member_ids
            L_names=[]
            for id in L_ids:
                L_names.append(self.get_user_name(id))
            return L_names

    def join_group(self,channel_name: str, user_name: str) -> None:
        member_id=self.get_user_id(user_name)
        j=0
        L_channels=self.channels
        while L_channels[j].name!=channel_name:
            j=j+1
        if j==(len(L_channels)+1):
            print("ce groupe n'existe pas")
        else:
            L_channels[j].member_ids.append(member_id)
            self.channels=L_channels
        self.save()

    def post_messages(self, channel: str, content: str, sender: str):
         channel_id=self.get_channel_id(channel)
         sender_id=self.get_user_id(sender)
         reception_date=str(datetime.now())
         id = max([message.id for message in self.messages])+1

         new_message=Message(id,reception_date,sender_id, channel_id,content)
         self.messages.append(new_message)

         self.save()

