def pascal(n):
    """
    :param n: Int -- Levels of pascal triangle

    :return: List[List[Int]] -- a list of sublists, which contains pascal values.
    """
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        first = [1]
        next = pascal(n - 1)
        last = next[-1]
        for i in range(len(last) - 1):
            first.append(last[i] + last[i + 1])
        first += [1]
        next.append(first)
        
    return next

def main():
    print(pascal(4))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

if __name__ == '__main__':
    main()