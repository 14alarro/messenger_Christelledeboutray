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

print('=== Messenger ===')
print('1. See users')
print('2. See channel')
print('x.Leave')
print('n. create user')
print('x. Main menu')
print(' ')

print(' ')


choice = input('Select an option: ')
while choice !='x':
    if choice == 'x':
        print('Bye!')
    elif choice == '1':
        print('Select an option: 1')
        print('User list')
        print('--------')
        for users in server['users']:
            print(users['name'])
    elif choice == '2':
        for message in server['messages']:
            print(message['content'])
    elif choice =='n':
        id=len(server['users'])
        id=server['users'][-1]['id']+1
        nom=input("donner un nom d'utilisateur")
        server['users'].append({'id': id, 'name': nom})
        print(server)
        print(server['users'])
    elif choice =='x.':
        for key in server:
            print(key)

    else:
        input("taper une commande répertoriée")
    choice = input('Select an option: ')