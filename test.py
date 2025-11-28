import os
import csv
os.chdir('exercise_10/Homework_12')
with open('students.csv') as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i)
