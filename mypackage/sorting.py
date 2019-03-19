#

def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    change = True
    passitem = len(items)-1
    while passitem > 0 and change:
        change = False
        for i in range(passitem):
            if items[i]>items[i+1]:
                change = True
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
        passitem = passitem-1
    return passitem




# the merge function

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''


    if len(items) <= 1:
        return items
# Find the middle point and devide it
    middle = len(items) // 2
    left_list = items[:middle]
    right_list = items[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


  # sorting

  def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

    n_list = []
    n_list = sorted(items)

    return n_list
