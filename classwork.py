class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"

p1 = Person("Otar", 34)

def serialize_person(person, filename):
    line = f"Name: {person.name}, Age: {person.age}"
    with open(filename, "w") as f:
        f.write(line)

def deserialize_person(filename):
    with open(filename, "r") as f:
        line = f.readline().strip()
    parts = line.split(", ")
    name_part = parts[0].split(": ")[1]
    age_part = int(parts[1].split(": ")[1])
    
    return Person(name_part, age_part)

serialize_person(p1, "person.txt")
p2 = deserialize_person("person.txt")
print(p2)

