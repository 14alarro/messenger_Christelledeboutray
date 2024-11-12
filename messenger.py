from datetime import datetime
server = {
    'users': [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ],
    'channels': [
        {'id': 1, 'name': 'Town square', 'member_ids': [1, 2]}
    ],
    'messages': [
        {
            'id': 1,
            'reception_date': "2019-14-04",
            'sender_id': 1,
            'channel': 1,
            'content': 'Hi '
        }
    ]
}

def ouverture_fichier():
    import json
    with open('server.json','r') as f:
        server=json.load(f)

ouverture_fichier()


def modif():
    with open('server.json', 'w') as f:
        json.dump(server, f,indent=10)


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
    n=len(server['users'])
    for i in range(n):
        print(i,'.',server['users'][i]["name"])
    print('n. Create user')
    print('x. Main menu')


def fonction_channel():
    for groupe in server['channels']:
        print(groupe['id'],groupe['name'])
    print("x. main menu")
    print("n. ajouter un groupe")


# max([mes['id'] for mess in server['messages]])+1
def fonction_add_user():
    id=len(server['users'])
    id=max([user['id'] for user in server['users']])+1
    #il aurait été plus judicieux de prendre le maximum des identifiants de la liste 
    #id=max[ i for for in server['users']+1], structure comme ça
    nom=input("donner un nom d'utilisateur")
    server['users'].append({'id': id, 'name': nom})
    print(server)
    print(server['users'])
    modif()


ecran_accueil()

def fonction_groupe():
    nom_groupe=input("donner moi le nom du groupe")
    membre=input('donner moi les gens membres du groupe')
    L=membre.split(',')
    L=[user.strip() for user in membre.split(',')]
    dico={}
    dico['id']=max([channels['id']for channels in server["channels"]])+1
    dico['name']=nom_groupe
    L_members=[]
    for members in L:
        i=0
        while server['users'][i]['name']!=members:
            i=i+1
        L_members.append(server['users'][i]['id'])
    dico['members_ids']=L_members
    server["channels"].append(dico)
    modif()

def ajout_membre_groupe():
    groupe=input('donner moi le nom du groupe')
    personne=input('donner moi le nom de la nouvelle personne')
    i=0
    while server['users'][i]['name']!=personne:
        i=i+1
    id=server['users'][i]['id']
    j=0
    while server['channels'][j]['name']!=groupe:
        j=j+1
    id=server['channels'][j]['id']
    server["channels"][j]['member_ids'].append(id)
    modif()
    print(server)

choice = input('Select an option: ')
while choice !='x':
    if choice == 'x':
        fonction_x()
    elif choice == '1':
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
            choice=input('select an option')
        ecran_accueil()
    elif choice =='x':
        print('Bye') 
    else:
        input("taper une commande répertoriée")
    choice = input('Select an option: ')


