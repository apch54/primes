from primes_module import init_primes_data_file, last_prime_in_data
from primes_module import is_prime_basic, is_prime, primes_nb_in_file_data
from primes_module import init_big_primes_file
from math import sqrt
from chrono_module import Chrono

"""
test big number as 2**n-1 as prime
"""
init_big_primes_file()


def big_prime(n):
    pn = big = 2**n - 1
    P = int(last_prime_in_data())
    max_P = P**2

    if big > max_P:
        raise Exception("Primes too big for this installation")
    larg = 2500  # numbers ok interval to estimate distance between 2 prime numberspos = 0
    pos = 0
    X = []

    while pos < larg:
        pos += 1
        if is_prime(pn):
            X.append(pn)
        pn += 2

    moy = (X[-1] - big) / len(X)
    return n, moy


data = open("primes_big_data", "r")
b = data.readlines()
last_big_data = int(b[-2])
last_big_data += 1
data.close()

print(last_big_data)
data = open("primes_big_data", "a")
ch = Chrono(900)  # time of calculation in sec

while ch.delta_t():
    bd = big_prime(last_big_data)
    data.write(str(bd[0]) + "\n")
    data.write(str(bd[1]) + "\n")
    print(bd)
    last_big_data += 1

data.close()
print("--  Terminé --")
