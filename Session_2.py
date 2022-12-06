class Teacher:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def teacher_detail(self):
        print("The name of teacher is ", self.name)
        print("The salary of teacher is ", self.salary)

name = input("Enter name of teacher")
salary = float(input("Enter salary of teacher"))
obj = Teacher(name,salary)
obj.teacher_detail()