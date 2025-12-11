# 1. ტრანზაქცია
class User:
    @staticmethod
    def validation(balance,pay):
        if balance < 0 and pay < 0:
            raise Exception('cant be negatice integers')
        if not isinstance(balance, (int,float)) and not isinstance(pay,(int,float)):
            raise ValueError('it cant be string')

    def __init__(self,balance,pay):
        User.validation(balance,pay)
        self.balance = balance
        self.pay = pay

    @staticmethod
    def tax(func):
        def wrapper(self):
            final = func(self)
            self.balance -= 1
            print('transaction is succesful')
            return self.balance
        return wrapper

    @tax
    def transaction(self):
        if self.balance < self.pay:
            print('not enough money')
        else:
            self.balance = self.balance - self.pay
            return self.balance

user = User(1500, 1000)
user.transaction()
print(user.balance)

# 2. private და protected მეთოდების არსებობა კლასში
class MetaVal(type):
    def __new__(cls,name,bases,dct):
        new_class = super().__new__(cls,name,bases,dct)
        for method in dct:
            if '_' not in method[0:2]:
                raise ValueError('missing _')
        return new_class

class Test(metaclass=MetaVal):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def test(self):
        pass

