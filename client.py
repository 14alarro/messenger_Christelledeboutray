
from localserver import LocalServer
from model import User
from remoteserver import RemoteServer
import sys
sys.stdout.reconfigure(encoding='utf-8')


class Client:
    def __init__(self, server: 'LocalServer | RemoteServer'):
        self.server=server

    def __repr__(self) -> str:
        # Les fonctions `__repr__` doivent renvoyer une chaîne
        # de caractères, pas l'afficher
        return f"Client(server={self.server})"

    @staticmethod
    def ecran_accueil():
        print('=== Messenger ===')
        print('1. See users')
        print('2. See channel')
        print("3. See messages")
        print('x.Leave')
        print(' ')

    @staticmethod
    def leave():
        print('Bye!')

    def fonction_user(self):
        print('Select an option: 1')
        print('User list')
        print('--------')
        server=self.server
        print(server.get_users()) 
        print('n. Create user')
        print('x. Main menu')

    def fonction_channel(self):
        server=self.server
        print("la liste des groupes est",server.get_channels())
        print("x. main menu")
        print("n. créer un groupe")
        print("m. voir les membres d'un groupe")
        print('u. ajouter un utilisateur à un groupe existant')

    def fonction_messages(self):
        print(self.server.get_messages())
        print('n create messages')
        print('x. Main menu')

    # Votre fonction est très longue, a beaucoup de niveaux
    # d'indentation, et une logique compliquée.
    # Vous pouvez la simplifier en la découpant en petites
    # fonctions avec des noms explicites.
    # Pour découper vos fonctions, une bonne pratique est de vous
    # rapprocher des concepts que l'utilisateur manipule.
    # Ici, l'utilisateur navigue d'un écran ou d'une liste à l'autre :
    # vous pouvez donc faire une fonction par écran.
    def welcome_screen(self):
        self.ecran_accueil()
        choice = input('Select an option: ')
        if choice == 'x':
            self.fonction_x()
        elif choice == '1':
            self.see_users()
        elif choice == '2':
            self.see_channels()
        elif choice=='3':
            self.see_messages()
        else:
            choice=input("taper une commande répertoriée")
            self.welcome_screen()

    # J'ai récupéré les 3 prochaines fonctions dans votre fonction
    # `welcome_screen`
    def see_users(self):
        print("execution fonction user")
        self.fonction_user()
        choice=input('select an option')
        while choice!='x':
            if choice == 'n':
                nom=input("donne moi le nom de l'utilisateur que tu veux créer")
                server=self.server
                server.add_user(nom)
            choice=input('select an option')
        self.ecran_accueil()

    def see_channels(self):
        self.fonction_channel()
        choice=input('select an option')
        while choice!='x':
            if choice == 'n':
                nom=input("donne moi le nom du groupe que tu veux créer")
                self.server.create_channel(nom)
            elif choice=='u':
                channel=input("donne moi le nom du groupe auquel tu veux ajouter quelqu'un")
                user=input("donne moi le nom de la personne que tu veux ajouter au groupe")
                self.server.join_group(channel,user)
            elif choice=='m':
                pass
            else:
                print("entrer une commande répertoriée")
            choice=input('select an option')
        self.ecran_accueil()

    def see_messages(self):
        self.fonction_messages()
        choice=input('select an option')
        while choice!='x':
            if choice == 'n':
                channel=input("donne moi le nom du groupe sur lequel tu veux poster un message")
                sender=input("donne moi le nom de la personne qui envoie le message")
                content=input("donne moi message que tu veux poster")
                self.server.post_messages(channel,content,sender)

            else:
                print('taper une commande répertoriée')
            choice=input('select an option')
