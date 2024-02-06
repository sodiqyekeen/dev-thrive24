class Skills:
    def __init__(self, id, Skill_Name, Description):
        self.id = id
        self.Skill_Name = Skill_Name
        self.Description = Description
    
    def __dict__(self):
        return {
            'id': self.id,
            'name': self.Skill_Name,
            'description': self.Description
        }

    def get_id(self):
        return self.id

    def get_Skill_Name(self):
        return self.Skill_Name
    
    def get_Description(self):
        return self.Description