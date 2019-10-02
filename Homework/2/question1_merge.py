def merge(I1, I2):  
    """
    takes two iterable objects and merges them alternately
    required runtime: O(len(I1) + len(I2)).

    :param I1: Iterable -- the first iterable object. Can be a string, tuple, etc
    :param I2: Iterable -- the second iterable object. Can be a string, tuple, etc

    :return: List -- alternately merged I1, I2 elements in a list.
    """      
    ret_lst = []
    first = True
    
    if len(I1) > len(I2):
        check = len(I1)
    else:
        check = len(I2)
        first = False
        
    for each in range(check):
        if first == True:
            ret_lst.append(I1[each])
            try: ret_lst.append(I2[each])
            except: pass
        else:
            try: ret_lst.append(I1[each])
            except: pass
            ret_lst.append(I2[each])
            
    return ret_lst

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print([i for i in merge("what",range(100,105))])
    print([i for i in merge(range(5),range(100,101))])
    print([i for i in merge(range(1),range(100,105))])

#if __name__ == '__main__':
#    main()