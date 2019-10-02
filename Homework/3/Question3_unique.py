def unique(s):
    """
    :param s: List[Any] -- list of values.
    :return: True if all values within s are unique.
             False otherwise.
    """
    if len(s) == 1:
        return True
    
    for next in s[1:]:
        if s[0] == next:
            return False
        unique(s[1:len(s)])
    return True
        
def main():
    print(unique([1,7,6,5,4,3,1]))   # False
    print(unique([9,4,3,2,1,8]))     # True
    print(unique(['9',[],4,3,2,1,8]))     # True

if __name__ == '__main__':
    main()