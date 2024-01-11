class Department:
    def __init__(self, id, name, faculty_id):
        self.id = id
        self.name = name
        self.faculty_id = faculty_id

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_faculty_id(self):
        return self.faculty_id