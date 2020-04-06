#Visualizacao de dados em python

import matplotlib.pyplot as plt 

x = [1,3,5,7,9]
y = [2,3,7,1,0]
#titulo = "Grafico de barras"
#eixox = "Eixo x"
#eixoy = "Eixo y"

#Legendas
#plt.title(titulo)
#plt.xlabel(eixox)
#plt.ylabel(eixoy)

#grafico de barra
#plt.bar(x, y, label = "Grupo 1")
#plt.show()


#grafico simples de linha
#plt.plot(x,y)
#plt.show()


#Comparar 2 graficos

x1 = [2,4,6,8,10]
y1 = [5,1,3,7,4]
#titulo1 = "Grafico de barras 2"
#eixox1 = "Eixo x1"
#eixoy1 = "Eixo y1"

#plt.bar(x1, y, label = "Grupo 2")
#plt.legend()
#plt.show()

#Grafico de dispersao

titulo = "Grafico de dispersao"
eixox = "Eixo x"
eixoy = "Eixo y"

plt.scatter(x,y, label = "Grafico de dispersao", color = "red", marker = ".", s = 20)
plt.plot(x,y, color = "green", linestyle = "--", linewidth = 2)
plt.legend()
plt.show()

'''
CORES (color)
'b' blue
'g' green
'r' red
'c' cyan
'm' magenta
'y' yellow
'k' black
'w' white

MARCADORES (marker)
'.' point marker
',' pixel marker
'o'	circle marker
'v'	triangle_down marker
'^'	triangle_up marker
'<'	triangle_left marker
'>'	triangle_right marker
'1'	tri_down marker
'2'	tri_up marker
'3'	tri_left marker
'4'	tri_right marker
's'	square marker
'p'	pentagon marker
'*'	star marker
'h'	hexagon1 marker
'H'	hexagon2 marker
'+'	plus marker
'x'	x marker
'D'	diamond marker
'd'	thin_diamond marker
'|'	vline marker
'_'	hline marker

TIPOS DE LINHA
'-'	 solid line style
'--' dashed line style
'-.' dash-dot line style
':'	 dotted line style
'''




