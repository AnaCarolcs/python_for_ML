entrada = open("original/bacteria.fasta").read()
saida = open("original/bacteria.html","w")

contador = {}

for i in ['A', 'T', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		contador[i+j] = 0

#print (contador)

entrada = entrada.replace("\n","")

#print (entrada)

for k in range(len(entrada)-1):
	contador[entrada[k] + entrada[k+1]] += 1 #ta com erro e nao to sabendo resolver

print(contador)

#html

i = 1
for k in contador:
	transparencia = contador[k]/max(contador.values())
	said.write("div style='width:100px, border:1px solid #111; height:100px; float:left; background-color:rgba(0,0,255,"+str(transparencia)+")')>"+k+"</div>")
	if 1%4 == 0:
		saida.write("<div style='clear:both'></div>")
	i+=1

saida.close()
