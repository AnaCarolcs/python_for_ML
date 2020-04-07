entrada = open("original/bacteria.fasta").read()
saida = open("original/bacteria.html", "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		cont[i+j] = 0

entrada = entrada.replace("\n","")

for k in range(len(entrada)-1):
	cont[entrada[k]+entrada[k+1]] += 1

print(cont)