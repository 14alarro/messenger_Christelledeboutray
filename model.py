class User:
    def __init__(self,id:int, name:str):
        self.name=name
        self.id=id
    def __repr__(self):
        return (f"User(name={self.name}, identifiant={self.id})")
    def to_dict(self):
        return{"id":self.id,"name":self.name}

class Channel:
    def __init__(self,id:int,member_ids:list,name:str):
        self.id=id
        self.name=name
        self.member_ids=member_ids
    def to_dict(self):
        return {'id':self.id,'name':self.name,'member_ids':self.member_ids}
    
class Message:
    def __init__(self, id: int, reception_date: str, sender_id: int, channel: int, content: str):
        self.id=id
        self.reception_date=reception_date
        self.sender_id = sender_id
        self.channel=channel
        self.content=content
    def __repr__(self):
        return(f"Message(identifiant={self.id}), channel={self.channel},content={self.content} ")
    def to_dict(self):
        return {'id':self.id, 'reception_date':self.reception_date, 'sender_id': self.sender_id, 'channel':self.channel,'content':self.content}