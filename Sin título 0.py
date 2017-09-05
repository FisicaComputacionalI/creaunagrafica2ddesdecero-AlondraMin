import numpy as np
import pylab as pl
#Crea un vector (arreglo) con los valores del eje X
x=[1,2,3,4]
#Crea un vector (arreglo) con valores en el eje Y para cada valor en el eje X
y=[8,9.2,8.5,8.5]
#Grafica del vector x contra el vector y
pl.plot(x,y)
pl.ylabel('Promedio')
pl.xlabel('Semestre')
pl.title('Promedio por semestre')
#Guarda la grafica
pl.savefig('temp1.png')