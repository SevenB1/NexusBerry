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