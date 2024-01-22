class Notification:
    def __init__(self, id,user_id,content):
        self.id = id
        self.user_id = user_id
        self.content = content

    def get_id(self):
        return self.id
    
    def get_user_id(self):
        return self.user_id
    
    def get_content(self):
        return self.content

