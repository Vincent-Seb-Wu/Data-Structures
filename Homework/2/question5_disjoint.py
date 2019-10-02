def three_way_disjoint(l1, l2, l3):
    """
    :param l1: List -- the first list of elements
    :param l2: List -- the second list of elements
    :param l3: List -- the third list of elements

    :return: True if l1,l2,l3 are disjoint.
    False if l1,l2,l3 are not disjoint.
    """
    lst = l1 + l2 + l3
    
    merge_sort(lst)
    check = lst[0]
    for each in range(len(lst)):
        if each + 1 == len(lst):
            break
        if check == lst[each + 1]:
            return False
        check = lst[each]
    return True

def merge_sort(lst):
    
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    l1 = [1,2,3,4,5]
    l2 = [6,7,8,9,10,11,12]
    l3 = [5,13,14,15,16]
    l4 = [5,6,7,8,9,10,11]
    
    print(three_way_disjoint(l1,l2,l3))   # True, yes three way disjoint.
    print(three_way_disjoint(l1,l4,l3))   # False, not three way disjoint.

if __name__ == '__main__':
    main()