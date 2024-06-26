class Student:
    def _init_(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def _repr_(self):
        return f"Student(student_id={self.student_id}, name={self.name}, age={self.age})"

def create_students():
    students_dict = {}
    
    num_students = int(input("Enter the number of students to create: "))
    
    for i in range(num_students):
        student_id = input(f"Enter ID for student {i+1}: ")
        name = input(f"Enter name for student {i+1}: ")
        age = int(input(f"Enter age for student {i+1}: "))
        
        student = Student(student_id, name, age)
        students_dict[student_id] = student
    
    return students_dict


students = create_students()
for student_id, student in students.items():
    print(f"ID: {student_id}, {student}")
