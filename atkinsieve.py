import math
def atkin(entry):
    """
    Returns a list of prime numbers below the number "entry":
    In the algorithm:
    All remainders are modulo-sixty remainders (divide the number by 2*2*3*5=60 and return the remainder). Using modulo-sixty we can easily see how it will skip multiples of 2, 3, and 5.
    All numbers, including x and y, are positive integers.
    Flipping an entry in the sieve list means to change the marking (prime or nonprime that translates to True and False respectively) to the opposite marking.
    This results in numbers with an odd number of solutions to the corresponding equation being potentially prime (prime if they are also square free),
    and numbers with an even number of solutions being composite(non primes).
    """
    #Initially, create a sieve dictionary with an entry for each positive integer; all entries of this list should initially be marked non prime (False, composite).
    sieveload = dict([(i, False) for i in range(5, entry+1)])
    #For each entry number n in the sieve list, with modulo-sixty remainder r :"
    for x in range(1, int(math.sqrt(entry))+1):
        for y in range(1, int(math.sqrt(entry))+1):
            n = 4*x**2 + y**2 
            #If r is 1,5 flip the entry for each possible solution to 4x^2 + y^2 = n
            if (n <= entry) and ((n % 12 == 1) or (n % 12 == 5)):
                sieveload[n] = not sieveload[n]
            n = 3*x**2 + y**2
            #If r is 7 flip the entry for each possible solution to 3x^2 + y2 = n 
            if (n <= entry) and (n % 12 == 7):
                sieveload[n] = not sieveload[n]
            n = 3*x**2 - y**2
            #If r is 11 flip the entry for each possible solution to 3x2 − y2 = n when x > y
            if (x > y) and (n <= entry) and (n % 12 == 11):
                sieveload[n] = not sieveload[n]
    #Start with the lowest number in the sieve list. Take the next number in the sieve list still marked prime. Include the number in the results list. Square the number and mark all multiples of that square as non prime. Note that the multiples that can be factored by 2, 3, or 5 need not be marked, as these will be ignored in the final enumeration of primes.
    for n in range(5, int(math.sqrt(entry))+1):
        if sieveload[n]:
            ik = 1
            while (ik * n**2 <= entry):
                #i^2, i^2+i, i^2+2*i, i^2+3*i, ... , not exceeding n
                sieveload[ik * n**2] = False
                ik += 1      
    #Create a list with all the results from the sieve and exclude the numbers 0,1,4     
    primes = []
    for i in range(entry + 1):
        if i in [0, 1, 4]: pass
        elif i in [2,3] or sieveload[i]:
             primes.append(i)
        else: pass
    return primes