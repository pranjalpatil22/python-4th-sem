
class course:
    def __init__(self,course,course_id,credits,teachingHours):
        self.course = course,
        self.course_id = course_id,
        self.credits = credits,
        self.teachingHours = teachingHours

    def getter(self):
        return f"courses: {self.course} , course id : {self.course_id} , credits : {self.credits} ,teachingHours : {self.teachingHours}"