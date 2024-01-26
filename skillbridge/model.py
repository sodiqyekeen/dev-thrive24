class Faculty:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

class Department:
    def __init__(self, id, department_name, faculty_id):
        self.id = id
        self.department_name = department_name
        self.faculty_id = faculty_id

    def get_id(self):
        return self.id

    def get_department_name(self):
        return self.department_name

    def get_faculty_id(self):
        return self.faculty_id

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

    def get_matric_no(self):
        return self.matric_no

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_department_id(self):
        return self.department_id

    def get_level(self):
        return self.level

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email


