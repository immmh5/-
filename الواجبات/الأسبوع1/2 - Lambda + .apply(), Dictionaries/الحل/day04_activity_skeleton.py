

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

print(students["S001"]["courses"]["AI301"]["grade"])

b = students["S002"]["courses"]
print(f"Bob: {sum(g['grade']*g['credits'] for g in b.values())/sum(g['credits'] for g in b.values()):.2f}")

print([students[s]["name"] for s in students if "CS101" in students[s]["courses"]])

g = [g["grade"] for s in students.values() for g in s["courses"].values()]
print(f"Avg: {sum(g)/len(g):.2f}")

top = max(students, key=lambda s: sum(g["grade"]*g["credits"] for g in students[s]["courses"].values())/sum(g["credits"] for g in students[s]["courses"].values()))
print(f"Top: {students[top]['name']}")