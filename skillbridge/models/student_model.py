class Student:
    def __init__(self, id, matric_no, first_name, last_name, department_id, level, username, password, email):
        self.id = id
        self.matric_no = matric_no
        self.first_name = first_name
        self.last_name = last_name
        self.department_id = department_id
        self.level = level
        self.username = username
        self.password = password
        self.email = email
    


    def get_id(self):
        return self.id
    
    def get_student(self, id):
        return {"id":self.id,
                "First name": self.first_name,
                 "Last name": self.last_name,
                  "Matric Number": self.matric_no,
                   "Username": self.username,
                    "email": self.email }

    def get_matric_no(self):
        return self.matric_no
    
    def get_full_name(self):
        return self.first_name, self.last_name
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_matric_no(self):
        return self.matric_no
    
    def get_username(self):
        return self.username
    
    def get_level(self):
        return self.level
    
    def get_password(self):
        return self.password
    
    def get_email(self):
        return self.email
    

