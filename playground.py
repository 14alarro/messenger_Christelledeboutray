
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

class User:
    def _init_(self,id:int, name:str):
        self.name=name
        self.id=id


user=User(1,'Alice')
print(user.name)

L_user=[]
for user in server['users']:
    id=user['id']
    name=user['name']
    element=User(id,user)
    L_user.append(element)
