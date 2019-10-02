def vc_count(word):
    """
    ### Friendly tip: This function can't solve the problem, 
    ### you need more parameters to pass information between recursive functions.
    ### So, define another function!! Return the result from your new function!!
    
    :param word: String -- the input string
    :return: List[Int] -- the first integer is the number of vowels, 
                          the second integer is the number of consonants.
    """
    return count(word)

def count(word, num = 0, v = 0, c = 0):
    if num == len(word):
        return [v, c]
    
    if word[num] in "aeiouAEIOU":
        v += 1
        num += 1
        return count(word, num, v, c)
    else:
        c += 1
        num += 1
        return count(word, num, v, c)

def main():
    print(vc_count("GoodMorningShanghai"))   # [7, 12]
    print(vc_count("WhatsUpGuys"))           # [3, 8]
    print(vc_count("EnjoyNationalHoliday"))  # [9, 11]
    print(vc_count("aaaaaaaaaaaaaaaAAAAA"))  # [20, 0]
    print(vc_count("hmmmmmmmmmmmmmmm"))      # [0, 16]

if __name__ == '__main__':
    main()