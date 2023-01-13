class Student:

    def __init__(self):

        self.first_name = 'ABC'

        self.last_name = 'DEF'

    def print_name(self):
        print('{0} {1} is a student in middle school.'.format(self.first_name, self.last_name))

student1 = Student()

student1.first_name = 'Alex'

student1.last_name = 'Smith'

student1.print_name()
