class Student:
    def __init__(self, name, ID, course):
        self.name = name
        self.ID = ID
        self.course = course

    def __repr__(self):
        return f"{self.name} - {self.ID}"


text = input()
students = []
while ":" in text:
    data = text.split(":")
    name = data[0]
    id = data[1]
    course = data[2]
    student = Student(name, id, course )
    students.append(student)

    text = input()
text = text.replace("_", " ")

for student in students:
    if student.course == text:
        print(student)
