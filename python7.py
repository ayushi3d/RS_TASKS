#student record using dictionary
student_record = {}
n = int(input("Enter the number of students: "))
for i in range(n):
    name=input("Enter student name: ")
    marks=int(input("Enter student marks: "))
    student_record[name]=marks
print("Student Record:")
for name, marks in student_record.items():
    print(f"{name}: {marks}")
    