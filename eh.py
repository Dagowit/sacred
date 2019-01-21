import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
import pandas as pd

czestProbkowania=200
dane = pd.read_csv("data.csv", delimiter=',', engine='python')
t = np.linspace (0, 37.914, 200*37.914)
sygnal=dane['a2']
przefiltrowany=ag.pasmowozaporowy(sygnal, czestProbkowania, 49,51)
przefiltrowany2=ag.pasmowoprzepustowy(przefiltrowany, czestProbkowania, 1,50)
plt.plot(t, przefiltrowany2)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()
liczba = []
for i in range (7582):
    if przefiltrowany2[i] > 0.05:
        liczba.append(przefiltrowany2[i])
print(liczba)
