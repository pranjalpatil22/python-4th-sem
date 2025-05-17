
class student:
    def __init__(self,name,id,semester,contact):
        self.name = name
        self.id = id
        self.semester = semester
        self.contact = contact

    def getter(self):
        return f"name s: {self.name} , id : {self.id} , semester : {self.semester} ,contact : {self.contact}"
