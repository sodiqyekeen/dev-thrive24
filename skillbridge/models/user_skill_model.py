class User_Skill:
    def __init__(self, id, Proficiency_level, student_ID, Skill_ID):
        self.id = id
        self.Proficiency_level = Proficiency_level
        self.student_ID = student_ID
        self.Skill_ID = Skill_ID

    def __dict__(self):
        return {
            'id': self.id,
            'proficiency_level': self.Proficiency_level,
            'Student_ID': self.student_ID,
            'Skill_ID': self.Skill_ID
        }

    def get_id(self):
        return self.id

    def get_Proficiency_level(self):
        return self.Proficiency_level

    def get_student1_ID(self):
        return self.student_ID
    
    def get_Skill_ID(self):
        return self.Skill_ID