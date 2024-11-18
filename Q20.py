#
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78), ('David', 92)]
student_dict = {name: score for name, score in students}
print("Students who scored above 80:")
for name, score in student_dict.items():
    if score > 80:
        print(name)