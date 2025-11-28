from random import randint
from functools import reduce

# 1. სორტირება
tuple_list = [(1, 3), (4, 2), (2, 5)]
print(sorted(tuple_list, key = lambda x:x[1]))

# 2. ლისტის გენერატორი 
list_condition = input('[length][lower bound][upper bound]>>> ').split()
def list_generator(l, lb, ub):
    generated_list = [randint(lb, ub) for _ in range(l)]
    try:
        index = int(input('[index]>>> '))
        result = lambda x: x[index]
        return result(generated_list)
    except IndexError:
        return f'element with position {index} is not in the list'
    except ValueError:
        return "index can't be a string"
    except Exception:
        return 'something wrong'

print(list_generator(int(list_condition[0]), int(list_condition[1]), int(list_condition[2])))

# 3. filter(), map(), sorted(), reduce() ფუნქციები
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]
print(list(filter(lambda x: x['price'] < 100, products)))
print(list(map(lambda x: f'{x.get('name')}: {x.get('price')}', products)))
print(sorted(products, key = lambda x: x['price']))
prices = []
for i in products:
    prices.append(i['price'])
print(reduce(lambda x,y: x + y, prices))

# 4. რეკურსიული ფუნქცია
num = int(input('[number]>>> '))
print(reduce(lambda x,y: x + y, list(range(1,num+1))))

