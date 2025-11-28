# 1. სიტყვების ჩანაცვლება
x =  input('წინადადება: ')
array = x.split()
array[0], array[1] = array[1], array[0]
print(array[0] + ' ' + array[1])

# 2. გრძელი სიტყვა
sentence = input('წინადადება: ')
new_array = sentence.split()
longest_word = ''
max_len = 0
for word in new_array:
    if len(word) > max_len:
        longest_word = word
        max_len = len(word)
print(longest_word)






 



