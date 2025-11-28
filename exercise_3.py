from random import randint
# 1.ყველა რიცხვის ჯამი და საშუალო არითმეტიკული 
el = [2,4,5,7,9]
s = 0
for i in el:
    s+=i
arm = s / len(el)
print(f'ყველა ელემენტის ჯამი და არითმეტიკული: {s} და {arm}')

# 2. უნიკალური ელემენტი
raw_list = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
filtered_list = []
for element in raw_list:
    if element not in filtered_list:
        filtered_list.append(element)
print(filtered_list)

# 3. 20 ელემენტიანი რიცხვების სია
list1 = [randint(-50, 50) for _ in range(1,21)]
list2 = [i for i in list1 if i % 2 == 0]
print(list1)
print(list2)

# 4. გრძელი და მოკლე სახელები
long_names = []
short_names = []
active = True
while active:
    user_input = input('შეიყვანეთ სახელი: ')
    if user_input == 'stop':
        active = False
    elif len(user_input) > 3:
        long_names.append(user_input.capitalize())
        print(long_names, short_names)
    else:
        short_names.append(user_input.capitalize())
        print(long_names, short_names)



