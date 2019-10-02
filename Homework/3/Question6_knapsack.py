import copy
def knapsack_driver(capacity, weights):
    '''
    @capacity: positive integer. the value we are summing up to.
    @weights:  list of positive integers.

    ### Friendly tip: This function can't solve the problem, 
    ### you need more parameters to pass information between recursive functions.
    ### So, define another function!! Return the result from your new function!!

    @return: List of all combinations that can add up to capacity.
    '''
    return driver(capacity, weights, [], 0, [])

def driver(capacity, weights, result, pos, answer):
    
    if pos >= len(weights):
        return 
    else:
        copy_ = copy.deepcopy(result)
        copy_.append(weights[pos])
        total = 0
        for each in copy_:
            total += each
        if total == capacity:
            answer.append(copy_)
        driver(capacity, weights, result, pos + 1, answer)
        driver(capacity, weights, copy_, pos + 1, answer)
        
    return answer
    
def main():   
    casts = [1, 2, 8, 4, 9, 1, 4, 5]
    # order does not matter, inner values order doesn't matter either.
    # [[9, 5], [9, 1, 4], [4, 1, 4, 5], [4, 9, 1], [8, 1, 5], [2, 8, 4], [2, 8, 4], [1, 9, 4], [1, 4, 4, 5], [1, 4, 9], [1, 8, 5], [1, 8, 1, 4], [1, 8, 4, 1]]
    print(knapsack_driver(14, casts))  

if __name__ == '__main__':
    main()