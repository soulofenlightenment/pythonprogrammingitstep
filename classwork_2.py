from faker import Faker
import random
import json

faker = Faker()
students = []
for _ in range(100):
    student = {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "age": random.randint(18, 70),
        "is_active": random.choice([True, False])
    }
    students.append(student)
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4)
with open("students.json", "r", encoding="utf-8") as f:
    students_data = json.load(f)
    
active_students = [s for s in students_data if s["is_active"]]

with open("active_students.json", "w", encoding="utf-8") as f:
    json.dump(active_students, f, indent=4)

