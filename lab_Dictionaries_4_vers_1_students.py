text = input()
courses = dict()
while ":"  in text:
    data = text.split(":")
    name = data[0]
    id = data[1]
    course = data[2]

    if course not in courses.keys():
        courses[course] = dict()

    courses[course][id] = name

    text = input()
text = text.replace("_", " ")

for id, name in courses[text].items():
    print(f"{name} - {id}")

