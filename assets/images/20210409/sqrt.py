def sqrt_binary(n, epsilon=0.000001):
    """ We only consider the positive sqrt here """
    # the ones that returns itself: 0, 1; need to cover 0.0 and 1.0 if enumerating 
    # if n in (0, 0.0, 0, 1.0):
    if n == 0 or n == 1:
        return n

    round = 0	
    left, right, guess = 0.0, n, n / 2.0
    while abs(guess * guess - n) > epsilon:
        guess = left + (right-left) / 2

        if guess * guess > n:
            right = guess
        else:
            left = guess
        
        round += 1	
    
    print('using binary, rounds are:', round)
    return guess

def sqrt_newton(n, epsilon=0.000001):
    """
    The square root of a given number n, with marginal room of epsilon
    """

    # Let's pivot using the input, for the sake of simplicity
    guess = n
    round = 0
    while abs(guess*guess - n) > epsilon:
        guess = guess - ((guess* guess - n)/(2*guess))
        round += 1
    
    print(f"For the square root of {n}, with precision of {epsilon}")
    print('Using newton approach, total rounds are:', round)
    return guess 


if __name__ == '__main__':
    print(sqrt_binary(2))
    print(sqrt_newton(2))
