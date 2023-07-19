import matplotlib.pyplot as plt

X, Y = [], []
big_data = open("primes_big_data", "r")
bd = big_data.readlines()
l = len(bd)

for i in range(0, l):
    if i % 2 == 0:
        X.append(int(bd[i]))
    else:
        Y.append(float(bd[i]))

# tracer de la courbe
plt.plot(X, Y, "r")
plt.grid(True)
plt.xlabel("n for 2**n-1")
plt.ylabel("Distance between 2 prime numbers near 2**n-1")
plt.title("Distance between 2 BIG prime numbers")
plt.show()
