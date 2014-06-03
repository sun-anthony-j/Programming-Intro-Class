# Name:
# Login:
# TA:
# Section:
# Q1.

# Mutable rlist
def mutable_rlist():
    """A mutable rlist that supports push, pop, and setitem operations.

    >>> a = mutable_rlist()
    >>> a('push', 3)
    >>> a('push', 2)
    >>> a('push', 1)
    >>> a('setitem', 1, 4)
    >>> a('str')
    '<rlist (1, 4, 3)>'
    """
    contents = empty_rlist

    def setitem(index, value):
        "*** YOUR CODE HERE ***"
        storage=empty_rlist
        for count in range(index+1):
            storage=rlist(dispatch('pop'),storage)
        dispatch('push',value)
        storage=rest(storage)
        while storage!=empty_rlist:
            dispatch('push',first(storage))
            storage=rest(storage)

    def dispatch(message, value=None, value2=None):
        nonlocal contents
        if message=='setitem':
            return setitem(value, value2)
        if message == 'first':
            return first(contents)
        if message == 'rest':
            return rest(contents)
        if message == 'len':
            return len_rlist(contents)
        if message == 'getitem':
            return getitem_rlist(contents, value)
        if message == 'str':
            return str_rlist(contents)
        if message == 'pop':
            item = first(contents)
            contents = rest(contents)
            return item
        if message == 'push':
            contents = rlist(value, contents)

    return dispatch

def pair(x, y):
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
    return dispatch

empty_rlist = None

def rlist(first, rest):
    return pair(first, rest)

def first(s):
    return s(0)

def rest(s):
    return s(1)

def len_rlist(s):
    if s == empty_rlist:
        return 0
    return 1 + len_rlist(rest(s))

def getitem_rlist(s, k):
    if k == 0:
        return first(s)
    return getitem_rlist(rest(s), k - 1)

def rlist_to_tuple(s):
    if s == empty_rlist:
        return ()
    return (first(s),) + rlist_to_tuple(rest(s))

def str_rlist(s):
    return '<rlist ' + str(rlist_to_tuple(s)) + '>'

# Q2.

class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('crab', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current crab stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your crab and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your crab.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, product, price):
        self.product=product
        self.price=price
        self.stock=0
        self.balance=0

    def vend(self):
        if self.stock==0:
            return 'Machine is out of stock.'
        elif self.balance<self.price:
            return 'You must deposit $'+str(self.price-self.balance)+' more.'
        else:
            self.stock+=-1
            change=self.balance-self.price
            self.balance=0
            if change>0:
                return 'Here is your '+str(self.product)+' and $'+str(change)+' change.'
            else:
                return 'Here is your '+str(self.product)+'.'

    def restock(self,amount):
        "Adds the amount of product to the stock"
        self.stock+=amount
        return 'Current '+str(self.product)+' stock: '+str(self.stock)

    def deposit(self, amount):
        if self.stock==0:
            return 'Machine is out of stock. Here is your $'+str(amount)+'.'
        else:
            self.balance+=amount
            return 'Current balance: $'+str(self.balance)


# Q3.

class MissManners(object):
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please.'
    >>> m.ask('please give up a teaspoon')
    'Thanks for asking, but I know not how to give up a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, InputFunction):
        self.InputFunction=InputFunction

    def ask(self, message,*args):
        if message[0:7]!='please ':
            return 'You must learn to say please.'

        elif hasattr(self.InputFunction, message[7:])==False:
            return 'Thanks for asking, but I know not how to '+message[7:]
        else:
            return getattr(self.InputFunction,message[7:])(*args)


# Q4.

class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> john = Account('John')
    >>> jack = Account('Jack')
    >>> john.deposit(10)
    10
    >>> john.deposit(5)
    15
    >>> john.interest
    0.02
    >>> jack.deposit(7)
    7
    >>> jack.deposit(5)
    12
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

"*** YOUR CODE HERE ***"

class SecureAccount (Account):
    def __init__(self, account_holder, password):
        self.password=password
        self.fails=0
        Account.__init__(self, account_holder)
    def withdraw(self,amount):
        return 'This account requires a password to withdraw'
    def secure_withdraw(self, amount, password):
        if self.fails>=3:
            return 'This account is locked'
        elif password!=self.password:
            self.fails+=1
            return 'Incorrect password'
        else:
            if amount > self.balance:
                return 'Insufficient funds'
            else:
                self.balance+= - amount
                return self.balance



import unittest

class SecureAccountTest(unittest.TestCase):
    """Test the SecureAccount class."""

    def setUp(self):
        self.account = SecureAccount('Alyssa P. Hacker', 'p4ssw0rd')

    def test_secure(self):
        acc = self.account
        acc.deposit(1000)
        self.assertEqual(acc.balance, 1000, 'Bank error! Incorrect balance')
        self.assertEqual(acc.withdraw(100),
                         'This account requires a password to withdraw')
        self.assertEqual(acc.secure_withdraw(100, 'p4ssw0rd'), 900,
                         "Didn't withdraw 100")
        self.assertEqual(acc.secure_withdraw(100, 'h4x0r'), 'Incorrect password')
        self.assertEqual(acc.secure_withdraw(100, 'n00b'), 'Incorrect password')
        self.assertEqual(acc.secure_withdraw(100, '1337'), 'Incorrect password')
        self.assertEqual(acc.balance, 900, 'Withdrew with bad password')
        self.assertEqual(acc.secure_withdraw(100, 'p4ssw0rd'),
                         'This account is locked')
        self.assertEqual(acc.balance, 900, 'Withdrew from locked account')

# Q5.

"*** YOUR CODE HERE ***"

class MoreSecureAccountTest(SecureAccountTest):
    """Test the MoreSecureAccount class."""

    def setUp(self):
        self.account = MoreSecureAccount('Alyssa P. Hacker', 'p4ssw0rd')

