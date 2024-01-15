class Project:
    def __init__(self, id, project_title, project_description, project_status):
        self.id = id
        self.project_title = project_title
        self.project_description = project_description
        self.project_status = project_status

    def get_id(self):
        return self.id
    
    def get_project_title(self):
        return self.project_title
    
    def get_project_description(self):
        return self.project_description
    
    def get_project_status(self):
        return self.project_status