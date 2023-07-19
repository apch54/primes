from primes_module import primes_nb_in_file_data, last_prime_in_data
from primes_module import twin_nb_in_file_data, last_twin_data

print("number of primes is {:_} ".format(primes_nb_in_file_data()))
print("last prime is {:_} ".format(last_prime_in_data()))
print("number of twin is {:_}".format(twin_nb_in_file_data()))
print("last twin is {:_} ".format(last_twin_data()))

Npv = 100  # nombre de valeurs pour le traçage de la courbe
Larg = 2000
Npn = round((twin_nb_in_file_data()- Larg) / Npv)   # nb primes between 2 main primes
print('_'*10,"{:_}".format(Npn))
x1 = 0
x2 , x3 = x1 + Npn, x1 + Larg
 
pn1, pos = 2, 0
X, Y = [2,], []
pn = open("primes_twin_data", "r")

while pos <= Npv * Npn:
    pn2 = pn.readline()
    pos += 1
    if pos == x3:
        y = (int(pn2) - int(pn1)) / Larg
        Y.append(y)
    if pos == x2:
        x1 = x2
        x2 += Npn
        x3 = x1 + Larg
        X.append(int(pn2))
        pn1 = pn2
X.pop()  # the last record is not avalable

pn.close()

# -----------------------------
# tracé de la courbe

import matplotlib.pyplot as plt

plt.plot(X, Y, "r")
plt.grid(True)
plt.xlabel("Values of twin numbers")
plt.ylabel("distance between 2 twin numbers")
plt.title("Distance beteen 2 twin numbers")
plt.show()
