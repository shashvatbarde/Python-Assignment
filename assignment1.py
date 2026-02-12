# 1) List to store names of 2 students
students = []

print("Enter details of 2 students")
for i in range(2):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name)

# 2) Tuple to store subjects (fixed subjects)
subjects = ("Maths", "Science", "English")

# 3) Dictionary to store each student's marks
marks = {}

for name in students:
    print(f"\nEnter marks for {name}:")
    student_marks = []
    
    for subject in subjects:
        mark = int(input(f"{subject}: "))
        student_marks.append(mark)
    
    marks[name] = student_marks

# 4) Set to find unique marks
all_marks = []
for m in marks.values():
    all_marks.extend(m)

unique_marks = set(all_marks)

# Displaying Output
print("\n----- OUTPUT -----")
print("Students List:", students)
print("Subjects Tuple:", subjects)
print("Marks Dictionary:", marks)
print("Unique Marks Set:", unique_marks)