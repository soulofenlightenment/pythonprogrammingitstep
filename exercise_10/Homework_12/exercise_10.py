import os
import csv
from faker import Faker
from random import randint
os.chdir('exercise_10/Homework_12')
# 1. პროგრამა, რომელიც ქმნის მონაცემთა ბაზას ტექსტური სახით და ამატებს მონაცემებს: ნომერს(id), სახელს და გვარს
active = True
while active:
    user_file = input('[file name]>>> ')
    fname_parsing = user_file.split('.')
    session = True
    if fname_parsing[len(fname_parsing)-1] == 'txt' and len(fname_parsing) != 1:
        while session:
            Id = 0
            user_name = input('[Name]>>> ').capitalize()
            user_lname = input('[Last Name]>>> ').capitalize()
            if user_name.lower() == 'stop':
                active = False
                session = False
            elif user_name.lower() == 'back' or user_lname.lower() == 'back':
                session = False
            else:
                try:
                    with open(user_file, 'r') as f:
                        lines = f.readlines()
                        Id = len(lines)
                except FileNotFoundError:
                    Id = 0
                with open(user_file, 'a') as f:
                    f.write(f'{Id + 1}. {user_name} {user_lname}\n')
    else:
        print('incorrect file exstension')

# 2. ფაილებში მონაცემების ფილტრაცია ასაკის მიხედვით
def age_filter(file, criteria):
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(f'greater_then_{criteria}.txt', 'a') as great, \
         open(f'less_then_{criteria}.txt', 'a') as less:
         for line in lines:
            if int(line.split(',')[1]) > criteria:
                great.write(line)
            elif int(line.split(',')[1]) < criteria:
                less.write(line)
            else:
                with open(f'equal_to_{criteria}', 'a') as equal:
                    equal.write(line)
active = True
while active:
        filter_file = input('[file (txt only)][filter by]>>> ') 
        if filter_file == 'exit':
            active = False
        else:
            try:
                filter_parsing = filter_file.split()
                file_name = filter_parsing[0]
                filter_by = int(filter_parsing[1])
            except ValueError:
                print(f'{filter_parsing[1]} is incorrect type')
            if file_name.split('.')[1] != 'txt':
                print('incorrect exstension')
            else:
                try:
                    age_filter(file_name, filter_by)
                except FileNotFoundError:
                    print('file with such name doesn\'t not exist')

# 3. 50 პიროვნება csv ფორმატით
fake = Faker()
def persons_50():
    field_names = ['ID','first_name','last_name','age']
    with open('persons_50.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        for i in range(1, 51):
            writer.writerow(
                {
                    'ID': i,
                    'first_name': fake.first_name(),
                    'last_name': fake.last_name(),
                    'age': randint(20, 80)
                }
            )
persons_50()

# 4. ქულების მიხედვით ფილტრაცია csv ფორმატით
def grade_filter():
    with open('students.csv', 'r') as f:
        reader = csv.DictReader(f)
        field = reader.fieldnames
        with open('passed.csv', 'w') as passed, \
            open('failed.csv', 'w') as failed:
            pwr = csv.DictWriter(passed,fieldnames=field)
            fwr = csv.DictWriter(failed,fieldnames=field)
            for row in reader:
                if int(row['Grade']) < 50:
                    fwr.writerow(row)
                else:
                    pwr.writerow(row)

grade_filter()






    
            


