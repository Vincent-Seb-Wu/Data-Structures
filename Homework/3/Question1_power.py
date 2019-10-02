def power(x,n):
    """
    Compute x^n, where x, n can both be negative integer.
    :param x: Int -- the base
    :param n: Int -- the exponent

    :return: Int -- x^n
    """
    
    if n == 0:
        return 1
    else:
        if n > 0:
            next = power(x, n // 2)
            result = next * next
            if n % 2 == 1:
                result *= x
            return result
        else:
            n *= -1
            next = power(x, n // 2)
            result = next * next
            if n % 2 == 1:
                result *= x
            return 1 / result



"""next = power(4, 3 // 2)
    next = power(4, 1 // 2)
        return 1
        next = 1
    result = next * next (1 * 1)
    if n % 2 == 1:
        result *= x (1 * 4)
    return result = 4
result = next * next (4 * 4)
if 3 % 2 == 1:
    result *= x (16 * 4)
    
return result
"""

def main():
    print(power(-2, 4))     # 16
    print(power(4, 3))      # 64
    print(power(-2, -3))    # -0.125

if __name__ == '__main__':
    main()