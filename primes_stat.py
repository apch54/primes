from primes_module import primes_nb_in_file_data

N = primes_nb_in_file_data()
print("N = {:_}".format(N))

Npv = 100  # nombre de valeurs pour le traçage de la courbe
Larg = 8_000
Npn = round((N - Larg) / Npv)  # 340_000  # nb primes between 2 main primes
x1 = 0
x2, x3 = x1 + Npn, x1 + Larg
pn1 = 2

X = []
X.append(2)
Y = []
pos = 0
pn = open("primes_data", "r")

while pos <= Npv * Npn:
    pn2 = pn.readline()
    pos += 1
    if pos == x3:
        y = (int(pn2) - int(pn1)) / Larg
        Y.append(y)
    if pos == x2:
        x1, x2 = x2, x2 + Npn
        x3 = x1 + Larg
        X.append(int(pn2))
        pn1 = pn2
X.pop()  # the last record is not valuable

print("X = ", X, "\ny = ", Y)
print("len(X) = ", len(X), "  ;  ", "len(Y) = ", len(Y))
pn.close()

# -----------------------------
# tracé de la courbe
import matplotlib.pyplot as plt

# import numpy as np

plt.plot(X, Y, "r")
plt.grid(True)
plt.xlabel("Values of prime numbers")
plt.ylabel("Distance between 2 prime numbers")
plt.title("Distance beteen 2 prime numbers")
# plt.xticks(np.arange(min(X), max(X) + 1, 5e6))
plt.show()
