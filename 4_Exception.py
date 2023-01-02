# class Error is derived from super class Exception
class Error(Exception):
    # Error is derived class for Exception, but
    # Base class for exceptions in this module
    pass


class TransitionError(Error):

    # Raised when an operation attempts a state
    # transition that's not allowed.
    #init is a contructor method in Python and is automatically called to allocate memory when a new object/instance is created.
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex

        # Error message thrown is saved in msg
        self.msg = msg
#The self parameter is a reference to the current instance of the class, and is used,
# to access variables that belongs to the class.

try:
    raise (TransitionError(2, 5 * 2, "Not Allowed"))

# Value of Exception is stored in error
except TransitionError as error:
    print('Exception occurred: ', error.msg)