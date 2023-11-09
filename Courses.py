class Courses:
    def __init__(self,course_code,course_title,credit_hours):
        self.course_code = course_code
        self.course_title = course_title
        self.credit_hours = credit_hours
    def list_all_courses():
        for course in Courses:
            print(course)

class Student:
    def __init__(self,reg_no,name):
        self.reg_no = reg_no
        self.name = name
        self.admitted_courses = []
    def admitted_courses(self):
        if self.admitted_courses:
            print(f"{self.name} is admitted to following courses")
            for course in self.admitted_courses:
                print(f"{Courses.course_title} with credit hours {Courses.credit_hours}")


python = Courses(2819,"Python Programming",400)
js = Courses(2814,"Javascript Programming",450)

Courses.list_all_courses()
