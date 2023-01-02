# class BalanceException is derived from super class Exception
class BalanceException(Exception):
    pass


def check_balance():
    money = 10000
    withdraw = int(input("Enter amount : "))
    balance = money - withdraw
    if balance < 1000:
        raise BalanceException('Insufficient balance')
    print(balance)


try:
    check_balance()
except BalanceException as be:
    print(be)

