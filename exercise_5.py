# 1. მომხმარებლის ასაკი
persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33), 
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]
active = True
while active:
    user_name = input('შეიყვანეთ სახელი: ').capitalize()
    user_lname = input('შეიყვანეეთ გვარი: ').capitalize()
    if user_name == 'Stop' or user_lname == 'Stop':
        active = False
    else:
        for person in persons:
            if user_name in person and user_lname in person:
                print(f'ასაკი: {person[2]}')

# 2. ვიპოვოთ ორ სიტყვათა სიმბოლოების თანაკვეთა, სიმეტრიული სხვაობა და გაერთიანება
char_set1 = set()
char_set2 = set()
word_1 = input("შეიყვანეთ პირველი სიტყვა: ").strip()
word_2 = input("შეიყვანეთ მეორე სიტყვა: ").strip()
for char1 in word_1:
    char_set1.add(char1)
for char2 in word_2:
    char_set2.add(char2)
common_chars = char_set1.intersection(char_set2)
unique_chars = char_set1.symmetric_difference(char_set2)
all_chars = char_set1.union(char_set2)
print(f'საერთო სიმბოლოები: {common_chars}\nუნიკალური სიმბოლოები: {unique_chars}\nყველა სიმბოლო: {all_chars}')