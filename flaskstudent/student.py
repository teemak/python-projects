class Student():

    counter = 1

    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = Student.counter
        Student.counter += 1
