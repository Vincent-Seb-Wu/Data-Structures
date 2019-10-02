def anagram(string1, string2):
    """
    :param string1: String -- the first python string.
    :param string2: String -- the second python string.

    :return: True if string1 is anagram of string2
             False otherwise.
    """
    # To do
    lst1 = []
    lst2 = []
    
    for each in string1:
        if each != " ":
            lst1.append(each)
    
    for each in string2:
        if each != " ":
            lst2.append(each)
            
    first = sorted(lst1)
    second = sorted(lst2)
    
    if first == second:
        return True
    return False

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

def main():
    string1 = "william shakespeare"
    string2 = "i am a weakish speller"
    print(anagram(string1, string2))   

    string1 = "software"
    string2 = "swear oft"
    print(anagram(string1, string2))  

if __name__ == '__main__':
    main()
