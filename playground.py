
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
    def __init__(self,id:int, name:str):
        self.name=name
        self.id=id


user=User(1,'Alice')




print(user.name)

L_users=[]
for user in server['users']:
    id=user['id']
    name=user['name']
    element=User(id,user)
    L_users.append(element)



class Server:
    def __init__(self,L_users,L_channels,L_messages):
        self.users=L_users
        self.channels=L_channels
        self.messages=L_messages

class Channel:
    def __init__(self,id:int,member_ids:list,name:str):
        self.id=id
        self.name=name
        self.member_ids=member_ids

L_channels=[]
for channel in server['channels']:
    id=channel['id']
    name=channel['name']
    member_ids=channel['member_ids']
    element=Channel(id,member_ids,name)
    L_users.append(element)


class Message:
    def __init__(self,id:int,reception_date:str,channel:int,content):
        self.id=id
        self.reception_date=reception_date
        self.channel=channel
        self.content=channel

L_messages=[]
for message in server['messages']:
    id=message['id']
    reception_date=message['reception_date']
    channel=message['channel']
    content=message['content']
    element=Message(id,member_ids,name,content)
    L_messages.append(element)



class Server:
    def __init__(self,L_users,L_channels,L_messages):
        self.users=L_users
        self.channels=L_channels
        self.messages=L_messages

server=Server(L_users,L_channels,L_messages)



