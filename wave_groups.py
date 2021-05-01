# Gera duas ondas de frequencias parecidas para mostrar a formacao de
# grupos de ondas

from numpy import *

close('all')

#Amplitude
a1 = 1
a2 = 1

#Periodos
T1 = 10
T2 = 11

f1 = 1/T1
f2 = 1/T2

L1 = 1.56 * T1**2
L2 = 1.56 * T2**2

#Vetor de tempo (1024 pontos)
t = arange(1,1025)

#Vetor de espaco
x = 1

#Fase
fase1 = 0
fase2 = 0

y1 = a1 * sin ( (2*pi/L1) * x + (2*pi/T1) * t + fase1 )
y2 = a1 * sin ( (2*pi/L2) * x + (2*pi/T2) * t + fase2 )

y = y1 + y2

plot(y)

#for i in range(len(t)):
#    
#    y1.append()