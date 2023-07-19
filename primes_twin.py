import primes_module as pm

N = pm.primes_nb_in_file_data()
print("Number of prime Numbers = ", N)
last_pn = pm.last_prime_in_data()
print("last prime is {:_}".format(int(last_pn)))

pm.init_twin_data_file()
Nt = pm.twin_nb_in_file_data()
print("NT = ", Nt)

# pm.last_twin_data()

N_research = 100000  # just to stop easily the program

pn1 = pm.last_twin_data()
pos = 1
PN = open("primes_data", "r")
PW = open("primes_twin_data", "a")
pn2 = PN.readline()

while int(pn2) != int(pn1):
    pn2 = PN.readline()
pn2 = PN.readline()

while pos < N_research:
    pos += 1
    pn2 = PN.readline()
    if int(pn2) - int(pn1) == 2:
        print(" pn2 = ", int(pn2), " pn1 = ", int(pn1))
        PW.write(pn1)
    pn1 = pn2

PN.close()
PW.close()

print("-" * 40)
N = pm.primes_nb_in_file_data()
print("Le nb de primes trouvé est {:_}".format(N))
print("NT = ", pm.twin_nb_in_file_data())
print("last twin is {:_}".format(pm.last_twin_data()))
