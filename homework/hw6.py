# Name: Anthony Sun
# Login: cs61a-mb
# TA: Mark Miyashita
# Section: 8-9:30 pm
# Q1.

def divide_by_fact(dividend, n):
    """Recursively divide dividend by the factorial of n.

    >>> divide_by_fact(120, 4)
    5.0
    """
    if n == 0:
        return dividend
    return divide_by_fact(dividend / n, n - 1)

# Q2.

def group(seq):
    """Divide a sequence of at least 12 elements into groups of 4 or
    5. Groups of 5 will be at the end. Returns a tuple of sequences, each
    corresponding to a group.

    >>> group(range(14))
    (range(0, 4), range(4, 9), range(9, 14))
    >>> group(tuple(range(17)))
    ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15, 16))
    """
    num = len(seq)
    assert num >= 12
    output=[]
    x=0
    "*** YOUR CODE HERE ***"
    if num%4==0:
        "no 5 tuple"
        x=0
        while x<num:
            output.append(seq[x:x+4])
            x+=4
        return tuple(output)
    elif num%4==1:
         x=0
         while x<num-5:
            output.append(seq[x:x+4])
            x+=4
         output.append(seq[x:x+5])
         return tuple(output)
    elif num%4==2:
        x=0
        while x<num-10:
            output.append(seq[x:x+4])
            x+=4
        output.append(seq[x:x+5])
        x+=5
        output.append(seq[x:x+5])
        return tuple(output)
    elif num%4==3:
        x=0
        while x<num-15:
            output.append(seq[x:x+4])
            x+=4
        output.append(seq[x:x+5])
        x+=5
        output.append(seq[x:x+5])
        x+=5
        output.append(seq[x:x+5])
        return tuple(output)

"""

   ====
    ==
========== <--- spatula underneath this crust
 ========

    ||
    ||
   \||/
    \/

========== }
    ==     } flipped
   ====    }
 ========

"""

# Q3.

def partial_reverse(lst, start):
    """Reverse part of a list in-place, starting with start up to the end of
    the list.

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    "*** YOUR CODE HERE ***"
    num=len(lst)
    index=0
    while index<((num-start)//2):
        lst[start+index],lst[num-1-index]= lst[num-1-index],lst[start+index]
        index+=1
    return
# Q4.

def index_largest(seq):
    """Return the index of the largest element in the sequence.

    >>> index_largest([8, 5, 7, 3 ,1])
    0
    >>> index_largest((4, 3, 7, 2, 1))
    2
    """
    assert len(seq) > 0
    "*** YOUR CODE HERE ***"
    x=max(seq)
    return seq.index(x)

# Q5.

def pizza_sort(lst):
    """Perform an in-place pizza sort on the given list, resulting in
    elements in descending order.

    >>> a = [8, 5, 7, 3, 1, 9, 2]
    >>> pizza_sort(a)
    >>> a
    [9, 8, 7, 5, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    def helper (lst2,index):
        """places the largest crust on the bottom"""
        if len(lst2[index:])==0:
            return
        partial_reverse(lst2,index+index_largest(lst2[index:]))
        partial_reverse(lst2,index)
        helper(lst2,index+1)
    helper(lst,0)
    return


# Q6.

def make_accumulator():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    "*** YOUR CODE HERE ***"
    lst=[]
    def accumulator(num):
        lst.append(num)
        total=0
        for x in range(len(lst)):
            total+=lst[x]
        return total
    return accumulator


# Q7.

def make_accumulator_nonlocal():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator_nonlocal()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator_nonlocal()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    "*** YOUR CODE HERE ***"

    total=0
    def accumulator(num):
        nonlocal total
        total+=num
        return total
    return accumulator

# Q8.

# Old version
def count_change(a, coins=(50, 25, 10, 5, 1)):
    if a == 0:
        return 1
    elif a < 0 or len(coins) == 0:
        return 0
    return count_change(a, coins[1:]) + count_change(a - coins[0], coins)

# Version 2.0
def make_count_change():
    """Return a function to efficiently count the number of ways to make
    change.

    >>> cc = make_count_change()
    >>> cc(500, (50, 25, 10, 5, 1))
    59576
    """
    "*** YOUR CODE HERE ***"


