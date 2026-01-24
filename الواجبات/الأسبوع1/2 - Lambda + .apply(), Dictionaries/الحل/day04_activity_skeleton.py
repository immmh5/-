students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}


print("--- Task 1: Alice's AI301 Grade ---")
alice_grade = students["S001"]["courses"]["AI301"]["grade"]
print(f"Alice's grade in AI301: {alice_grade}")


print("\n--- Task 2: Calculate Bob's GPA ---")
bob_courses = students["S002"]["courses"]
total_points = 0
total_credits = 0

for course_name, details in bob_courses.items():
    total_points += details["grade"] * details["credits"]
    total_credits += details["credits"]

bob_gpa = total_points / total_credits
print(f"Bob's GPA: {bob_gpa:.2f}")


print("\n--- Task 3: Find all students in CS101 ---")
cs101_students = []
for s_id, s_info in students.items():
    if "CS101" in s_info["courses"]:
        cs101_students.append(s_info["name"])

print(f"Students in CS101: {cs101_students}")


print("\n--- Task 4: Average grade across all courses ---")
all_grades = []
for s_info in students.values():
    for course in s_info["courses"].values():
        all_grades.append(course["grade"])

average_grade = sum(all_grades) / len(all_grades)
print(f"Average grade (Global): {average_grade:.2f}")


print("\n--- Task 5: Find student with highest GPA ---")
best_student = ""
highest_gpa = -1

for s_info in students.values():
    current_points = sum(c["grade"] * c["credits"] for c in s_info["courses"].values())
    current_credits = sum(c["credits"] for c in s_info["courses"].values())
    
    if current_credits > 0:
        current_gpa = current_points / current_credits
    else:
        current_gpa = 0
        
    if current_gpa > highest_gpa:
        highest_gpa = current_gpa
        best_student = s_info["name"]

print(f"Top Student: {best_student} with GPA: {highest_gpa:.2f}")

#😂تم صناعة هذا كله من قبل الذكاء الاصطناعي نرجوا من الجميع الدعاء له😂