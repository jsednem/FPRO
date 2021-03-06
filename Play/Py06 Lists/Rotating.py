"""
Write a Python function rotate_list(l) that, given a list l of length >= 3, shifts its elements to the left 3 times, returning the new list. If an element is at the beginning, it should circle back to the end.

    for the list l=[1,2,3,4,5,6], the result is the list [4,5,6,1,2,3]
    for the list l=[1,2,3,4,5,6,7,8], the result is the list [4,5,6,7,8,1,2,3]

Adapted from: CodingBat 
"""
def rotate_list(l):
    if len(l) >= 3:
        for x in l[:3]:
            l.remove(x)
            l.append(x)
    return l
