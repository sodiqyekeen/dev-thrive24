class Skill_Exchange:
    def __init__(self, id, student1_ID, student2_ID, skill_ID, Status):
        self.id = id
        self.student1_ID = student1_ID
        self.student2_ID = student2_ID
        self.skill_ID = skill_ID
        self.Status = Status
    
    def __dict__(self):
        return {
            'id': self.id,
            'student1_ID': self.student1_ID,
            'student2_ID': self.student2_ID,
            'skill_ID' : self.skill_ID,
            'status' : self.status
        }

    def get_id(self):
        return self.id

    def get_student1_ID(self):
        return self.student1_ID
 
    def get_student2_ID(self):
        return self.student2_ID
    
    def get_skill_ID(self):
        return self.skill_ID
    
    def get_Status(self):
        return self.Status