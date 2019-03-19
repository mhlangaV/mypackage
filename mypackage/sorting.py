#

def bubble_sort(items):

   '''Return array of items, sorted in ascending order'''

   bubbled_items = items.copy() # Making sure that the new list is of the same length as items
   for i in range(len(bubbled_items)):
       for j in range(len(bubbled_items)-1-i):
           if bubbled_items[j] > bubbled_items[j+1]:
               bubbled_items[j], bubbled_items[j+1] = bubbled_items[j+1], bubbled_items[j]

   return bubbled_items




# the merge function

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    len_i = len(items)
    # Base case. A list of size 1 is sorted.
    # Cae returns, so if reached then function will terminate after line 8
    if len_i == 1:
        return items
    # Recursive case. Find midpoint of list
    mid_point = int(len_i / 2)
    # divide list into two halves
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])
    # call merge_sort function on each half of list
    return merge(i1, i2)

# Merge function.
def merge(A, B):
    new_list = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list


  # sorting

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

    n_list = []
    n_list = sorted(items)

    return n_list
