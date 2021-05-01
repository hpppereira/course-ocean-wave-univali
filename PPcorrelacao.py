##Exercicio 1 - Analise de dados - Autocorrelacao


##importa modulos
from numpy import *
from pylab import *
import numpy as np

##fecha todas as figuras
close('all')

## funcao para correlacao: np.correlate

##Gerar serie aleatoria com 128 pontos e dt = 1s

a = rand(128)

##arquivo com serie randomica

#a = loadtxt('/home/henrique/Dropbox/Curso_Python_AD/a.txt')

##retira a media da serie

a = a - mean(a)

##funcao cosseno com 128 pontos, amp=1, freq=0,1, dt=1 -- w=2*pi*f

b = 1 * cos(2 * pi * 0.1 * (arange(1,129)))

##graficos das series

f1 = figure (1)
subplot(2,1,1)
plot(a), title('Serie aleatoria'), ylabel('Amplitude'), axis('tight'), grid('on')
subplot(2,1,2)
plot(b), title('Serie cosseno'), xlabel('Tempo (seg)'), ylabel('Amplitude'), axis('tight'), grid('on')
savefig('fig1')

##Series para autocorrelacao
c = a + 10 * b
d = a + b
e = a + 0.1 * b
f = a + 0.01 * b

##calcular e plotar as funcoes de autocorrelacao das series c, d, e, f

## help correlate
## 'full' e 'same' retornam um vetor de correlacao
## 'valid' retorna um valor de correlacao
## a full sai igual o default do matlab

cor1 = correlate(c,c,'full')

##pega apenas a metado do vetor, e divide pelo valor maximo da correlacao (ver com parente)
ccor = cor1[len(cor1)/2:] / max(cor1)

f2 = figure (2)
subplot(2,1,1)
plot(c,'-o'), axis('tight'), grid('on')
title(' Serie "c" ')
subplot(2,1,2)
plot(ccor,'-o'), axis('tight'), grid('on')
title('Autocorrelacao, serie "c" ')
xlabel('Defasagem')
savefig('fig2.png')

cor2 = correlate(d,d,'full')
dcor = cor2[len(cor2)/2:] / max(cor2)

f3 = figure (3)
subplot(2,1,1)
plot(d,'-o'), axis('tight'), grid('on')
title(' Serie "d" ')
subplot(2,1,2)
plot(dcor,'-o'), axis('tight'), grid('on')
title('Autocorrelacao, serie "d" ')
xlabel('Defasagem')
savefig('fig3.png')

cor3 = correlate(e,e,'full')
ecor = cor3[len(cor3)/2:] / max(cor3)

f4 = figure (4)
subplot(2,1,1)
plot(e,'-o'), axis('tight'), grid('on')
title(' Serie "e" ')
subplot(2,1,2)
plot(ecor,'-o'), axis('tight'), grid('on')
title('Autocorrelacao, serie "e" ')
xlabel('Defasagem')
savefig('fig4.png')

cor4 = correlate(f,f,'full')
fcor = cor4[len(cor4)/2:] / max(cor4)

f5 = figure (5)
subplot(2,1,1)
plot(f,'-o'), axis('tight'), grid('on')
title(' Serie "f" ')
subplot(2,1,2)
plot(fcor,'-o'), axis('tight'), grid('on')
title('Autocorrelacao, serie "f" ')
xlabel('Defasagem')
savefig('fig5.png')

w = loadtxt('C:\Users\hppp\Dropbox\Curso_Ondas_Univali\Rotinas_ADOG\Curso_Python_AD/w.txt')

w = w - mean(w)

w1 = w[0:128]
w2 = w[12:]

cor5 = correlate(w1,w2,'full')
# wcor = cor5[len(cor5)/2:] / max(cor5)
wcor = cor5 / max(cor5)

f6 = figure (6)
subplot(2,1,1)
plot(w1), plot(w2), axis('tight'), grid('on')
title(' Series "w1" e "w2" ')
subplot(2,1,2)
##deixa o eixo x com valores positivos e negativos (igual no matlab)
plot(arange(-len(wcor)/2,len(wcor)/2),wcor,'-o'), axis('tight'), grid('on')
title('Correlacao cruzada de w1 e w2')
xlabel('Defasagem')
savefig('fig6.png')

show()
