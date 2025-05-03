class User:
    def __init__(self,id:int, name:str):
        self.name=name
        self.id=id
    def __repr__(self) -> str:
        return (f"User(name={self.name}, identifiant={self.id})")
    def to_dict(self) -> dict:
        return{"id":self.id,"name":self.name}

    # Cette fonction peut vous être utile pour éviter de dupliquer
    # du code si vous avez besoin de construire des objets de la classe
    # `User` à plusieurs endroits.
    @classmethod
    def from_dict(cls, user_as_dict: dict) -> 'User':
        return cls(
            user_as_dict['id'],
            user_as_dict['name']
        )

class Channel:
    def __init__(self,id:int,member_ids:list,name:str):
        self.id=id
        self.name=name
        self.member_ids=member_ids
    def to_dict(self) -> dict:
        return {'id':self.id,'name':self.name,'member_ids':self.member_ids}

    @classmethod
    def from_dict(cls, channel_as_dict: dict) -> 'Channel':
        if 'member_ids' in channel_as_dict:
            member_ids = channel_as_dict['member_ids']
        else:
            member_ids = []
        return cls(
            channel_as_dict['id'],
            member_ids,
            channel_as_dict['name']
        )
    
class Message:
    def __init__(self, id: int, reception_date: str, sender_id: int, channel: int, content: str):
        self.id=id
        self.reception_date=reception_date
        self.sender_id = sender_id
        self.channel=channel
        self.content=content
    def __repr__(self) -> str:
        return(f"Message(identifiant={self.id}), channel={self.channel},content={self.content} ")
    def to_dict(self) -> dict:
        return {'id':self.id, 'reception_date':self.reception_date, 'sender_id': self.sender_id, 'channel':self.channel,'content':self.content}

    @classmethod
    def from_dict(cls, message_as_dict: dict) -> 'Message':
        return cls(
            message_as_dict['id'],
            message_as_dict['reception_date'],
            message_as_dict['sender_id'],
            message_as_dict['channel'],
            message_as_dict['content'],
        )
