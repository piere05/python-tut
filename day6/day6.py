# class car:
#     def __init__(self,name):
#         self.name=name

# car1 = car("TATA")
# car2 = car("Renout")
# print(car1.name)
# print(car2.name)


class InsufficientBalanceError(Exception):
    pass


bal = 1000
amt =1100

try:
    if amt > bal:
        raise InsufficientBalanceError("Not Sufficient Balance")
except InsufficientBalanceError as e:
    print(e)