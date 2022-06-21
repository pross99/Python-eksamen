class Bank:    
    def __init__(self):
        self.__accounts = []  # When bank is initialized it has  the abillity to hold many accounts
    
    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, acc):
        if type(acc) in [list, tuple, set]:
            for i in acc:
                self.__has_account(i)
                self.__accounts.append(i)
        else:
            self.__has_account(acc)
            self.__accounts.append(acc)

    def __has_account(self, acc):
        for i in self.__accounts:
            if acc.cust.name == i.cust.name:
                raise ValueError('Customer aleready has an account!')
        return False

class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust

    def __repr__(self):
        return str(self.__dict__)


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError('You must be 18 or above to create an account')
        self.__age = age

    def __repr__(self):
        return str(self.__dict__)