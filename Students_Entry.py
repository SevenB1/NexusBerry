# Students_List = []
# print("========== STUDENT ENTRY SYSTEM ==========")
# n = int(input("Number of Students: "))
# for i in range(n):
#     print("Student Id      Student Name         Subject 1     Subject 2     Subject 3")
#     student_info = input("Enter the information asked above separated by commas: ")
#     info = student_info.split()
#     students_list = info
#     Students_List.append(students_list)
# for i, students_list in enumerate(Students_List):
#     print(students_list)
student_records = []
print("========== STUDENT ENTRY SYSTEM ==========")
while True:
    student_info = {}

    student_info["ID"] = int(input("Enter student's ID: "))
    student_info["Name"] = input("Enter student's name: ")
    student_info["Chemistry"] = int(input("Enter student's marks in Chemistry: "))
    student_info["Biology"] = int(input("Enter student's marks in Biology: "))
    student_info["Physics"] = int(input("Enter student's marks in Physics: "))

    student_records.append(student_info)

    repeat = input("Do you want to add another student? (yes/no): ")
    if repeat != "yes" or repeat == "YES":
        break

print("\nStudent Id     Student Name     Chemistry     Biology     Physics")
for i,student in enumerate(student_records, 1):
    for key, value in student.items():
        print(f"{value}" ,end ="\t\t")
    print()