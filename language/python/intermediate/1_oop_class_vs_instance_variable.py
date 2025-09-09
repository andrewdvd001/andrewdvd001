class Student:
    school = "Global Academy"
    def __init__(self, name, list_of_completed_course = None):
        self.name = name
        if list_of_completed_course is None:
            self.list_of_completed_course = []
        else:
            self.list_of_completed_course = list_of_completed_course

    def complete_course(self, course_name):
        self.list_of_completed_course.append(course_name)

    def show_profile(self):
        print(f'Student name: {self.name}')
        print(f'Completed course: {", ".join(self.list_of_completed_course)}')
        print(f'School name: {Student.school}\n')

student1 = Student("Andrew", ["Python core"])
student2 = Student("David",)

student2.complete_course("Python Intermediate")
student1.show_profile()
student2.show_profile()