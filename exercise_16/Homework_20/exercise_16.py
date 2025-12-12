import json
from os import chdir
chdir('exercise_16/Homework_20')

def limit(n):
    return n
person = {
    "id": 0,
    "name": "",
    "age": 0
}
count = 0
user_period = int(input('limit of session: '))
while count < limit(user_period):
    name = input('enter your name: ')
    age = int(input('enter your age: '))

    with open('persons.json') as f:
        data = json.load(f)     
    Id = len(data) + 1

    person['id'] = Id; person['name'] = name; person['age'] = age
    data.append(person)
    
    with open('persons.json','w') as f:
        json.dump(data,f,indent=4)

    count+=1
 


