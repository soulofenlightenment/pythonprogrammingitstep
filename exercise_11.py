# Student კლასი

class Student:
    status = True
    pay = 1000
    
    def __init__(self,first_name,last_name,age,grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades 
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def get_discount(self):
        if self.age < 18:
            new_pay = self.pay - self.pay * (1/5)
            return f'u must pay {new_pay} because of your age'
        return f'you must pay {Student.pay}'
    def calculate_average(self):
        n = 0
        total = 0
        for grade in self.grades:
            total+=grade
            n+=1
        average = total/n
        return average
    def get_status(self):
        avg = self.calculate_average()
        if avg > 90:
            return 'exellent'
        elif 70 <= avg < 90:
            return 'good'
        elif 50 <= avg < 70:
            return 'average'
        else:
            self.status = False
            return 'poor' 
student_1 = Student('enki','ankarian', 30, [50,70,45,90,100,100])
student_2 = Student('d\'arce','cataliss', 14, [20,30,10,5,80,50])

print(student_1.full_name())
print(student_1.calculate_average())
print(student_1.get_discount())
print(student_1.get_status())
print(student_2.full_name())
print(student_2.calculate_average())
print(student_2.get_discount())
print(student_2.get_status())
print(student_2.get_discount())

