# 1. uppercase ფუნქცია
user_input = input('ტექსტი: ')
def uppercase(text):
    count = 0
    for char in text:
        if char.isupper():
            count+=1
    print(text.upper())
    return count
upper_text = uppercase(user_input)
print(f"uppercase characters: {upper_text}")

# 2. snake_case ფუნქცია
user = input("Camel: ")
def snake_case(text):
    words = []
    word = ''
    for char in text:
        if char.isupper():
            words.append(word)
            word = char
        else:
            word+=char
    if word:
        if len(words) == 0:
            print(text)
        else:
            words.append(word)
            snake = '_'.join(words)
            print(f'snake: {snake.lower()}')
snake_case(user)





