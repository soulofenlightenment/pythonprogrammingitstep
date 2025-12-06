class System_meta(type):
    __required_methods =['deposit','withdraw','check_balance']
    meta_account = {}
    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls,name,bases,dct)
        System_meta.meta_account[name] = new_class
        for required in System_meta.__required_methods:
            if required not in dct:
                raise TypeError(f'class {name} must have {required} method')
        return new_class

class Bank_account(metaclass=System_meta):
    bank_name = ''
    __total_accounts = 0
    
    @classmethod
    def get_total_accounts(cls):
        return Bank_account.__total_accounts

    @staticmethod
    def validate_amount(amount):
        if amount < 0 or type(amount) != int:
            return False
        else:
            return True

    def __init__(self,owner,balance):
        self._owner = owner
        if Bank_account.validate_amount(balance):
            self.__balance = balance
        Bank_account.__total_accounts += 1
        self.__account_number = f'AN{Bank_account.__total_accounts:04d}'
        

    def deposit(self, amount):
        if Bank_account.validate_amount(amount):
            self.__balance += amount
    def withdraw(self,amount):
        if Bank_account.validate_amount(amount):
            self.__balance -= amount
    def check_balance(self):
        return self.__balance
    def get_account_number(self):
        return self.__account_number
    def change_owner(self, new_owner):
        self._owner = new_owner
    def __str__(self):
        return f'{self.__account_number} | owner: {self._owner}'
        
Bank_account.bank_name = 'TBC'
acc_1 = Bank_account('otto', 1000)
print(acc_1)



