# fichier python que je n'utilise pas du tout mais que j'ai gardé pour garder une trace et au cas où


import json
from typing import List 
from model import Message, Channel,User



class Server:
    def __init__(self,SERVER_FILE_NAME):
        with open('server.json') as f:
            server=json.load(f)
            L_messages=[]
            for message in server['messages']:
                id=message['id']
                reception_date=message['reception_date']
                sender_id = message['sender_id']
                channel=message['channel']
                content=message['content']
                element = Message(id, reception_date, sender_id, channel, content)
                L_messages.append(element)
            L_channels=[]
            for channel in server['channels']:
                id=channel['id']
                name=channel['name']
                member_ids=channel['member_ids']
                element=Channel(id,member_ids,name)
                L_channels.append(element)
            L_users=[]
            for user in server['users']:
                id=user['id']
                name=user['name']
                element = User(id, name)
                L_users.append(element)
            self.users=L_users
            self.channels=L_channels
            self.messages=L_messages
    def __repr__(self):
        return(f"Server(users={self.users},channels={self.channels}, messages={self.messages}")
    def save(self):
        # fonction qui passe d'une classe à un dictionnaire afin de faire le json.dump
        serveur={}
        #server.users contient une somme d'objets 
        L_users=[user.to_dict() for user in self.users]
        serveur['users']=L_users
        L_channels=[channel.to_dict() for channel in self.channels]
        serveur["channels"]=L_channels
        L_messages=[message.to_dict() for message in self.messages]
        serveur["messages"]=L_messages
        with open('server.json', 'w') as f:
            json.dump(serveur, f,indent=10)
    @classmethod
    def load(cls):
        with open('server.json') as f:
            server=json.load(f)
            return cls(server)   
    def get_users(self)->List[User]:
        L_users=[]
        for user in self.server.users:
            L_users.append(user.name)
        return (L_users)
    def get_messages(self):
        L_messages=[message.to_dict() for message in self.messages]
        return (L_messages)
    def get_channels(self):
        L_channels=[channel.to_dict() for channel in self.channels]
        print(L_channels)




        




#créer une deuxième version, faire un appel réseau 
# il faut que l'on utilise les planches 


# version de server datant du 14 janvier
import json
class Server:
    def __init__(self,SERVER_FILE_NAME):
        with open('server.json') as f:
            server=json.load(f)
            L_messages=[]
            for message in server['messages']:
                id=message['id']
                reception_date=message['reception_date']
                sender_id = message['sender_id']
                channel=message['channel']
                content=message['content']
                element = Message(id, reception_date, sender_id, channel, content)
                L_messages.append(element)
            L_channels=[]
            for channel in server['channels']:
                id=channel['id']
                name=channel['name']
                member_ids=channel['member_ids']
                element=Channel(id,member_ids,name)
                L_channels.append(element)
            L_users=[]
            for user in server['users']:
                id=user['id']
                name=user['name']
                element = User(id, name)
                L_users.append(element)
            self.users=L_users
            self.channels=L_channels
            self.messages=L_messages
    def __repr__(self):
        return(f"Server(users={self.users},channels={self.channels}, messages={self.messages}")
    def save(self):
        # fonction qui passe d'une classe à un dictionnaire afin de faire le json.dump
        serveur={}
        #server.users contient une somme d'objets 
        L_users=[user.to_dict() for user in self.users]
        serveur['users']=L_users
        L_channels=[channel.to_dict() for channel in self.channels]
        serveur["channels"]=L_channels
        L_messages=[message.to_dict() for message in self.messages]
        serveur["messages"]=L_messages
        with open('server.json', 'w') as f:
            json.dump(serveur, f,indent=10)
    @classmethod
    def load(cls):
        with open('server.json') as f:
            server=json.load(f)
            return cls(server)



class Channel:
    def __init__(self,id:int,member_ids:list,name:str):
        self.id=id
        self.name=name
        self.member_ids=member_ids
    def to_dict(self):
        return {'id':self.id,'name':self.name,'member_ids':self.member_ids}

class Client:
    def __init__(self, server):
        self.server=server
    def __repr__(self):
        print(f"Client(server={self.server})")
    @ staticmethod
    def welcome_screen():
        def ecran_accueil():
            print('=== Messenger ===')
            print('1. See users')
            print('2. See channel')
            print('x.Leave')
            print(' ')

        def fonction_x():
            print('Bye!')

        def fonction_user():
            print('Select an option: 1')
            print('User list')
            print('--------')
            for user in server.users:
                print("le nom est")
                print(user.name)
            
            #for i in range(n):
                #print(i,'.',server['users'][i]["name"])
            print('n. Create user')
            print('x. Main menu')


        def fonction_channel():
            for groupe in server.channels:
                print(groupe.id,groupe.name)
            print("x. main menu")
            print("n. ajouter un groupe")
            print('u. ajouter un utilisateur')


        # max([mes['id'] for mess in server['messages]])+1
        def fonction_add_user():
            id=max([user.id for user in server.users])+1
            nom=input("donner un nom d'utilisateur")
            #modifier ici, mettre classe
            new_user=User(id,nom)
            server.users.append(new_user)
            server.save()




        def fonction_groupe():
            nom_groupe=input("donner moi le nom du groupe")
            membre=input('donner moi les gens membres du groupe')
            L=membre.split(',')
            L=[user.strip() for user in membre.split(',')]
            new_group_id = max([channel.id for channel in server.channels])+1
            L_members=[]
            for members in L:
                i=0
                while server.users[i].name != members:
                    i=i+1
                L_members.append(server.users[i].id)
            new_group = Channel(new_group_id, L_members, nom_groupe)
            server.channels.append(new_group)
            server.save()

        def fonction_add_user():
            id=max([user.id for user in server.users])+1
            nom=input("donner un nom d'utilisateur")
            #modifier ici, mettre classe
            new_user=User(id,nom)
            server.users.append(new_user)
            server.save()

        ecran_accueil()
        choice = input('Select an option: ')
        while choice !='x':
            if choice == 'x':
                fonction_x()
            elif choice == '1':
                print("execution fonction user")
                fonction_user()
                choice=input('select an option')
                while choice!='x':
                    if choice == 'n':
                        fonction_add_user()
                    choice=input('select an option')
                ecran_accueil()
                #choice=input('select an option')
            elif choice == '2':
                fonction_channel()
                choice=input('select an option')
                while choice!='x':
                    if choice == 'n':
                        fonction_groupe()
                    if choice=='u':
                        ajout_membre_groupe()
                    choice=input('select an option')
                ecran_accueil()
            elif choice =='x':
                print('Bye') 
            else:
                input("taper une commande répertoriée")
            choice = input('Select an option: ')




#SERVER_FILE_NAME = 'server.json'
#server = Server(SERVER_FILE_NAME)
#server.load()
#client = Client(server)
#client.welcome_screen()



# fonction à ranger dans une classe pour ajouter des membres à un groupe
def ajout_membre_groupe():
    groupe=input('donner moi le nom du groupe')
    personne=input('donner moi le nom de la nouvelle personne')
    L_users=server.users
    i=0
    while L_users[i].name!=personne and i<len(L_users):
        print(L_users[i].name)
        i=i+1
    if i==(len(L_users)):
        print("cette personne n'existe pas")
    else:
        member_ids=L_users[i].id  
    j=0
    L_channels=server.channels
    #ajouter une fonctionnalité de manière à avoir un message 
    while L_channels[j].name!=groupe:
        j=j+1
    if j==(len(L_channels)+1):
        print("ce groupe n'existe pas")
    else:
        channel=L_channels[j]
        channel.member_ids.append(member_ids)
    server.save()


# fonction add user qui était enregistrée dans la classe client
def add_user(self):
        id=max([user.id for user in self.server.users])+1
        nom=input("donner un nom d'utilisateur")
        #modifier ici, mettre classe
        new_user=User(id,nom)
        self.server.users.append(new_user)
        self.server.save()

        