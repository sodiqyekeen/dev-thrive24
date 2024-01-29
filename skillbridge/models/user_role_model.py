class USER_ROLE:
    def __init__(self,id,role_name):
        self.id = id
        self.role_name = role_name

    def get_id(self):
        return self.id
    
    def get_role_name(self):
        return self.role_name