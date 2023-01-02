class NegativeError(Exception):
    def _init_(self, data):
        self.data = data

    def _str_(self):
        return str(self.data) + ' is not a positive integer number'
#The self parameter is a reference to the current instance of the class, and is used,
# to access variables that belongs to the class.

try:
    x = int(input("Enter a positive integer number: "))
    if x < 0:
        raise NegativeError(x)
except NegativeError as e:
    print(e)
