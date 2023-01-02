class InventoryError(Exception):
    pass

class LocalToFarError(Exception):
    pass

def shedule_delivery(distance):
    if distance > 15:
        raise LocalToFarError('delivery available only within 15 km')

    else:
        print('order placed successfully. product will be deliverd soon')

def check_order(q):
    stock = 100
    if q > stock:
        raise InventoryError('insufficient stock:')
    else:
        d=int(input('enter the distance from store:'))
        shedule_delivery(d)


try:
    quantity = int(input('enter the requrired quantity'))
    check_order(quantity)
except InventoryError as ie:
    print(ie)
except LocalToFarError as le:
    print(le)