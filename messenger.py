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
            'reception_date': datetime.now(),
            'sender_id': 1,
            'channel': 1,
            'content': 'Hi '
        }
    ]
}
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
    for groupe in server['messages']:
        print(groupe['name'])

def fonction_add_user():
    id=len(server['users'])
    id=server['users'][-1]['id']+1
    nom=input("donner un nom d'utilisateur")
    server['users'].append({'id': id, 'name': nom})
    print(server)
    print(server['users'])


ecran_accueil()

def fonction_groupe():
    nom_groupe=input("donner moi le nom du groupe")
    membre=input('donner moi les gens membres du groupe')
    L=membre.split(',')
    dico={}
    dico['id']=server['channels'][-1]['id']+1
    dico['name']=nom_groupe
    L_members=[]
    for members in L:
        i=0
        while server['users'][i]['name']!=members:
            i=i+1
        L_members.append(server['users'][i]['id'])
    dico['members_ids']=L_members
    server["channels"].append(dico)

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
    elif choice == '2':
        fonction_channel()
    elif choice =='x':
        print('Bye') 
    else:
        input("taper une commande répertoriée")
    choice = input('Select an option: ')

