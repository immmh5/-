from day04_activity_skeleton import students

grade = students["S001"]["courses"]["AI301"]["grade"]
x = students["S002"]["courses"].values()
c = sum(c["grade"] * c["credits"] for c in x) / sum(c["credits"] for c in x)
students_101 = [s["name"] for s in students.values() if "CS101" in s["courses"]]
g = [c["grade"] for s in students.values() for c in s["courses"].values()]
all = sum(g) / len(g)
s = {s["name"]: sum(c["grade"]*c["credits"] for c in s["courses"].values()) / 
               sum(c["credits"] for c in s["courses"].values()) for s in students.values()}
top_student = max(s, key=s.get)
print(f"1: {grade} | 2: {c:.2} | 3: {students_101} | 4: {all:.2f} | 5: {top_student}")