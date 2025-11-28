# 1. ფაილის ფუნქცია
user_file = input('[Enter file name]>>> ')
user_word = input('[Enter word]>>> ')
def file_checker(file):
    count_lines = 0
    max_len = 0
    long_line = ''
    with open(file) as f:
        for lines in f:
            count_lines += 1
            if len(lines) > max_len:
                max_len = len(lines)
                long_line = lines
        f.seek(0)
        words = f.read().split()
        word_count = len(words)
    return f'lines: {count_lines}\nlongest line: {long_line}\nwords: {word_count}'
print(file_checker(user_file))

# 2. ფუნქცია რომელიც აბრუნებს იმის მნიშვნელობას თუ რამდენჯერ შეგვხვდა ჩვენ მიერ შეყვანილი სიტყვა ფაილში

def word_encounter(file, word):
    with open(file) as f:
        words = f.read().split()
        encounter = words.count(word)
        return f'word encountered: {encounter}'
print(word_encounter(user_file, user_word))