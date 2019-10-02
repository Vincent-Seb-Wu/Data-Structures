def vigenere_encrypt(plain, key):
    """
    :param plain: String -- a python input string. The plain text.
    :param key: String -- a python input string. The key.

    :return: String -- the cipher python string text.
    """
    # To do
    key *= (len(plain) // len(key)) + 1
    new_string = []
    
    for each in range(len(plain)):
        sub = ord(key[each]) - 65
        new = sub + ord(plain[each])
        if new > 90:
            new_string.append(chr((new - 90) + 64))
        else:
            new_string.append(chr(new))
    
    return "".join(new_string)

def vigenere_decrypt(cipher, key):
    '''
    :param cipher: String -- a python input string. The cipher text.
    :param key: String -- a python input string. The key.

    :return: String -- the plain python string text.
    '''
    # To do
    key *= (len(cipher) // len(key)) + 1    
    new_string = []
    
    for each in range(len(cipher)):
        sub = ord(key[each]) - 65
        new = ord(cipher[each]) - sub
        if new < 65:
            new_string.append(chr(91 - (65 - new)))
        else:
            new_string.append(chr(new))
        
    return "".join(new_string)


'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(vigenere_encrypt("ATTACKATDAWN", "NYUSH"))   # NRNSJXYNVHJL

    print(vigenere_encrypt("DATASTRUCTURE", "NYUSH"))   # QYNSZGPOUAHPY

    print(vigenere_encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NYUSH"))  # NZWVLSEBAQXJGFVCOLKAHTQPFM

    print(vigenere_encrypt("CUTE", "NYUSH"))  # PSNW

    print(vigenere_decrypt("NRNSJXYNVHJL", "NYUSH"))   # ATTACKATDAWN
    print(vigenere_decrypt("QYNSZGPOUAHPY", "NYUSH"))   # DATASTRUCTURE
    print(vigenere_decrypt("NZWVLSEBAQXJGFVCOLKAHTQPFM", "NYUSH"))   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(vigenere_decrypt("PSNW", "NYUSH"))  # CUTE

if __name__ == '__main__':
    main()
