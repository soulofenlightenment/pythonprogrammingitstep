# 1. ჯამის ფუნქცია
n = input('element number: ')
def nth_element_sum(nth):
    elements = []
    sums = 0
    if nth == '':
        nth = 0
        while nth < 5:
            element = int(input('element: '))
            elements.append(element)
            nth+=1
        for i in elements:
            sums+=i
        return sums
    else:
        x = 0
        while x < int(nth):
            element = int(input('element: '))
            elements.append(element)
            x+=1
        for i in elements:
            sums+=i
        return sums
print(nth_element_sum(n)) 
            
# 2. ლუწი და კენტი რიცხვების ლისტები
def odd_even_sorter(*args):
    odd = []
    even = []
    for i in args:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd,even
print(odd_even_sorter(2,3,4,5,6))

# 3. სიტყვების დამთვლელი ფუნქცია
user_input = input(">>> ").lower()
def count_words(sentence):
    words = []
    count_data = {}
    if sentence == '' or sentence == ' ':
        return "please enter a sentence"
    else:
        for word in sentence.split():
            if "," in word or '.' in word:
               new_word = word.replace(',', '').replace('.', '')
               words.append(new_word)
            else:
                words.append(word)
        for word in words:
            reference = words.count(word)
            count_data.update({word: reference})
        return count_data
print(count_words(user_input))

