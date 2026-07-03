class user :
    def __init__(self):
        self.name = 'krishna'
        self.gender = 'Male'

    def login(self):
        print("User logged in")


class student(user):

  

    def enroll(self):
        print("Student enrolled")

u = user()
s = student()

print(s.name)
s.login()
s.enroll()