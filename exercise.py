# 1. 5 ფაქტორიალი(5!)
n = int(input('factorial of: '))
res = 1
for i in range(1,n+1):
     res *= i
print(res)

# 2. გამრავლების ტაბულა
dec1 = dec2 = [i for i in range(1,10)]
for i in dec1:
     for j in dec2:
          res = i * j
          print(f'{i} * {j} = {res}')

# 3. აპარატი
active = True
tax = 50
valid_marks = [5,10,20]
while active:
     user_input = int(input('შეიყვანეთ თანხა: '))
     if user_input in valid_marks:  
          tax-=user_input
          if tax > 0:
               print(f'დარჩენილია თანხა: {tax}')
          else:
               print('თანხა დაფარულია')
               active = False
     else:
          print('შეიტანეთ შესაბამისი კუპიურები')
     
          

 