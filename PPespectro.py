##calculo do espectro

#Desenvolvido por:
# Henrique Patricio P. Pereira
# E-mail: henriqueppp@oceanica.ufrj.br
# Data da ultima modificacao: 11/11/2013


##importa modulos
from pylab import *
from numpy import *

close('all')

##cria onda senoidal

##tempo
t = arange(1024)
#amplitude
a = 0.5

##frequencia
w1 = 2 * pi * 0.1
w2 = 2 * pi * 0.25

sen1 = a * cos (w1 * t)
#sen2 = a * cos (w2 * t)

onda = sen1 #+ sen2

##espectro

dt = 1

freq = fft.fftfreq(onda.size , dt)
freq = freq[0:len(freq)/2]
##para comecar de 0.00097 (ficar igual a subrotina espectro. qual esta certo?)
freq = freq + 0.00097

ps = 2 * abs(fft.fft(onda)**2) / 1024
ps = ps[0:len(ps)/2]


##calculo pelo rotina espectro
import espectro

gl = 2
han = 0

aa = espectro.espec1(onda,dt,gl,han)

freq1 = aa[:,0]
ps1 = aa[:,1]

figure ()
plot(freq,ps,'b-*')
plot(freq1,ps1,'r-*')

## calcula o espectro para onda simulada com hs = 2 m, tp = 12, dir = 45 graus

#dados = loadtxt('/home/henrique/Dropbox/analise_de_dados_Python/1_registro45.txt')
#dados = loadtxt('/home/henrique/Dropbox/analise_de_dados_Python/200905010800.txt')
dados = loadtxt('C:\Users\hppp\Dropbox\Curso_Ondas_Univali\Rotinas_ADOG\ADOG_05_espectro/200905010800.txt')


#col 1 quando for o dado real e 0 para o simulado
eta = dados[0:1024,1]

figure()
plot(eta)

feta = fft.fftfreq(eta.size , dt)
feta = feta[0:len(feta)/2]
##para comecar de 0.00097 (ficar igual a subrotina espectro. qual esta certo?)
feta = feta + 0.00097

pseta = 2 * abs(fft.fft(eta)**2) / 1024
pseta = pseta[0:len(pseta)/2]


#calculo pela rotina espectro, funcao espec1

gl = 32
han = 0

aa1 = espectro.espec1(eta,dt,gl,han)

f1eta = aa1[:,0]
ps1eta = aa1[:,1]

figure ()
plot(feta,pseta,'b-*')
plot(f1eta,ps1eta,'r-*')

##calculo do periodo de pico (onda real)
tp = 1 / f1eta[find(ps1eta==max(ps1eta))]

##calculo da altura significativa (onda real)
m0 = sum(ps1eta) * (f1eta[1]-f1eta[0])
hm0 = 4.01 * sqrt(m0)


##calculo do periodo de pico (onda senoidal)
tps = 1 / freq[find(ps==max(ps))]

##calculo da altura significativa (onda senoidal)
m0s = sum(ps) * (freq[1]-freq[0])
hm0s = 4.01 * sqrt(m0s)


show()
