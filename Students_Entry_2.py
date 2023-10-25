student_data = {}

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    student_id = input(f"Enter Student ID for student {i + 1}: ")
    
    while student_id in student_data:
        print(f"Student ID {student_id} already exists. Please enter a unique ID.")
        student_id = input(f"Enter Student ID for student {i + 1}: ")
    
    chemistry_score = float(input(f"Enter the chemistry score for student {student_id}: "))
    biology_score = float(input(f"Enter the biology score for student {student_id}: "))
    physics_score = float(input(f"Enter the physics score for student {student_id}: "))
    
    student_scores = {
        "Chemistry": chemistry_score,
        "Biology": biology_score,
        "Physics": physics_score
    }
    
    student_data[student_id] = student_scores

print("\nStudent Data Table:")
print(f"{'Student ID':<15}{'Chemistry':<10}{'Biology':<10}{'Physics':<10}")
print("=" * 50)

for student_id, scores in student_data.items():
    chemistry_score = scores["Chemistry"]
    biology_score = scores["Biology"]
    physics_score = scores["Physics"]
     
    print(f"{student_id:<15}{chemistry_score:<10.2f}{biology_score:<10.2f}{physics_score:<10.2f}")
