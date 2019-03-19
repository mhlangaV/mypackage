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
    x = 1
    for i in range(n,0,-1):
         x = x *i
    return x



def reverse(word):

    '''Return word in reverse'''

    string = ""
    for i in word:
        string = i+string
    return string
