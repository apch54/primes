"""                                                  
 _____     _                              _     _     
|  _  |___|_|_____ ___ ___    _____ ___ _| |_ _| |___ 
|   __|  _| |     | -_|_ -|  |     | . | . | | | | -_|
|__|  |_| |_|_|_|_|___|___|  |_|_|_|___|___|___|_|___|
                                                      
"""
from os.path import exists
from math import sqrt

first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
first_twin = [3, 5, 11, 17, 29]
first_big = [4, 7.089, 5, 7.110, 6, 7.183, 7, 7.257]


def init_big_primes_file():
    if not exists("primes_big_data"):
        data = open("primes_big_data", "a")
        for p in first_big:
            data.write(str(p) + "\n")
        data.close


def init_primes_data_file():
    if not exists("primes_data"):
        data = open("primes_data", "a")
        for p in first_primes:
            data.write(str(p) + "\n")
            # print(p)
        data.close()


def init_twin_data_file():
    if not exists("primes_twin_data"):
        tw = open("primes_twin_data", "a")
        for p in first_twin:
            tw.write(str(p) + "\n")
            # print(p)
        tw.close()


def last_prime_in_data():
    primes_file = open("primes_data", "r")
    last_prime = int(primes_file.readlines()[-1])
    primes_file.close()
    return last_prime


def last_twin_data():
    primes_twin_file = open("primes_twin_data", "r")
    last_twin = int(primes_twin_file.readlines()[-1])
    primes_twin_file.close()
    return last_twin


def is_prime_basic(nbr):
    """
    Determine if nbr (int) is a prime number
    or not ; return a boolean
    """
    sq = sqrt(nbr)
    if nbr % 2 == 0:
        return False  # not a prime
    i = 3
    while i < sq:
        if nbr % i == 0:
            # print('facteur : '+str(i) )
            return False  # not prime
        i += 2
    return True  # a prime number


def is_prime(nbr):
    """
    determine if nbr is prime or not.
    Algorithme more efficient.
    use prime_data file
    """
    sq = sqrt(nbr)
    pms = open("primes_data", "r")
    pm = pms.readline()

    while int(pm) < sq:
        if nbr % int(pm) == 0:
            # print(int(pm), "  ", nbr % int(pm), "  ", sq)
            return False  # not prime nbr
        pm = pms.readline()

    pms.close()
    return True  # is prime nbr


def primes_nb_in_file_data():
    """
    return the nb of primes in primes_data file
    """
    with open("primes_data") as f:
        text = f.readlines()
        f.close()
        return len(text)


def twin_nb_in_file_data():
    """
    return the nb of twin primes in primes_data file
    """
    with open("primes_twin_data") as f:
        text = f.readlines()
        f.close()
        return len(text)


if __name__ == "__main__":
    print(first_primes)

    nbr = 20228053
    if is_prime_basic(nbr):
        print(nbr, " is a prime nbr.")
    else:
        print(nbr, " is NOT a prime nbr.")
    print(last_prime_in_data(), "  ", sqrt(nbr))
    init_big_primes_file()
