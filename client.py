
from model import User

class Client:
    def __init__(self, server):
        self.server=server
    def __repr__(self):
        print(f"Client(server={self.server})")
    def welcome_screen(self):
        server=self.server
    def ecran_accueil():
        print('=== Messenger ===')
        print('1. See users')
        print('2. See channel')
        print('x.Leave')
        print(' ')

    def fonction_x():
        print('Bye!')

    def fonction_user(self):
        print('Select an option: 1')
        print('User list')
        print('--------')
        for user in self.server.users:
            print("le nom est")
            print(user.name)
        
        #for i in range(n):
            #print(i,'.',server['users'][i]["name"])
        print('n. Create user')
        print('x. Main menu')


    def fonction_channel(self):
        for groupe in self.server.channels:
            print(groupe.id,groupe.name)
        print("x. main menu")
        print("n. ajouter un groupe")
        print('u. ajouter un utilisateur')


    # max([mes['id'] for mess in server['messages]])+1
    def fonction_add_user(self):
        id=max([user.id for user in server.users])+1
        nom=input("donner un nom d'utilisateur")
        #modifier ici, mettre classe
        new_user=User(id,nom)
        self.server.users.append(new_user)
        self.server.save()

