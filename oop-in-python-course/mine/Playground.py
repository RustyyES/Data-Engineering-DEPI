"""class TrackedProperty:
    def __init__(self, name, var=None):
        self.name = name
        self.private_name = f"_{name}"
        self.var = var

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        print(f"{self.name} name accessed")
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)


class Variable:
    dog = TrackedProperty("dog")
    cat = TrackedProperty("cat")
    owner = TrackedProperty("owner")
    user_count = 0

    def __init__(self, dog_name, cat_name, owner_name):
        self._dog = dog_name
        self._cat = cat_name
        self._owner = owner_name
        Variable.user_count += 1


x = Variable(" ", " ", " ")
y = Variable(" ", " ", " ")
print(Variable.user_count)"""


class BankAccount:
    MIN_Balance = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @staticmethod
    def is_valid_interest(rate):
        return rate


bank = BankAccount("omar")
print(bank.is_valid_interest(5))
