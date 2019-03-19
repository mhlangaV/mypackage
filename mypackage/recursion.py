# the sum_array function get an array and return the sum of the array

def sum_array(array):

    '''Return sum of all items in array'''
    return sum(array)


#

def fibonacci(n):

   """
   Calculate nth term in fibonacci sequence

   Args:
       n (int): nth term in fibonacci sequence to calculate

   Returns:
       int: nth term of fibonacci sequence,
            equal to sum of previous two terms
   """

   if n <= 1:
       return n
   if n == 2:
       return 1
   else:
       return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):

   '''Returns the product of all positive integers less than or equal to n.'''

   if n < 0:
       raise ValueError(" n must be a positive integer")

   elif n == 0:
       return 1

   elif n == 1:
       return n

   else:
       return  n * factorial(n-1)

def reverse(word):

    '''Return word in reverse'''

    string = ""
    for i in word:
        string = i+string
    return string
