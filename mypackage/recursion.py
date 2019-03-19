# the sum_array function get an array and return the sum of the array

def sum_array(array):

    '''Return sum of all items in array'''
    return sum(array)


#

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    x,y = 1,1
    for i in range(n-1):
        x,y = y,x+y

    return x


def factorial(n):
    '''Return n!'''
    if n == 1:
        return n
    else:
        lower_fact = factorial(n-1)
        current_fact = n * lower_fact
        return  current_fact


def reverse(word):

    '''Return word in reverse'''

    string = ""
    for i in word:
        string = i+string
    return string
