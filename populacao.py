#crescimento da populacao brasileira de 1980 ate 2016

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
	if i != 0:
		linha = dados[i].split(";")
		x.append(int(linha[0]))
		y.append(int(linha[1]))

#print (x)
#print (y)

plt.plot(x,y)
plt.title("Populacao brasileira")
plt.xlabel("Ano")
plt.ylabel("Populacao")
plt.show()

#plt.savefig("populacao_brasileira.png", dpi=300)