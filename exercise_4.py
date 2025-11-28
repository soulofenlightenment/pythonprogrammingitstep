# 1. კვადრატები ლექსიკონში
square_elements = {i:i**2 for i in range(1,10)}
print(square_elements)

# 2. პროდუქტების (ა. დასახელება, ბ. ღირებულებების ჯამი)
products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10
    }},
    {"fanta": {
        "price": 2.5,
        "quantity": 5
    }},
    {"snickers": {
        "price": 3.5,
        "quantity": 12
    }},
    {"water": {
        "price": 4.5,
        "quantity": 8
    }},
    {"beer": {
        "price": 6.5,
        "quantity": 5
    }}
]

# ა. პროდუქტების დასახელება
products_names = [list(i.keys())[0] for i in products]
print(products_names)
# ბ. პროდუქტების ღირებულებების ჯამი
s = 0
for i in range(0,len(products)):
    s += products[i][products_names[i]]['price'] * products[i][products_names[i]]['quantity']
print(f'სულ: {s}')

# 3. ხილის დასახელება და შეყვანილი ხილის რაოდენობა
active = True
items = {}
while active:
    user_input = input('Enter your favorite fruit: ')
    if user_input == 'stop':
        active = False
    if user_input in items.keys():
        items[user_input]+=1
    else:
        items[user_input] = 1
    print(items)


