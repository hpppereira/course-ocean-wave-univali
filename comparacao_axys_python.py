## Compara os dados reprocessados com o arquivo Summary, com
## os parametros calculados pela boia

#Verificar se mesmo com a data baguncada do arquivo Summary
#conseguimos coincidir as data utilizando o plot_date, ou 
#tentando ler os dados e fazer um 'sort'.

#pra isso precisamos aprender coloco ler string na funcao loadtxt

#importa bibliotecas
from numpy import *
from pylab import *
from datetime import datetime

close('all')

#carrega os dados

py = loadtxt('/home/hppp/Dropbox/Tese/PNBOIA_Processamento/HNE/Recife_HNE/Saida_Param_Axys_Recife.txt',skiprows = 1)
#      0   1   2    3   4  5   6   7    8     9     10   11 12  13 
#py = Ano Mes Dia Hora Min Hs H10 Hmax Tmed THmax HTmax Hm0 Tp DirTp

#carrega os parametros
ax = loadtxt('/home/hppp/Dropbox/Tese/PNBOIA_Processamento/HNE/Recife_HNE/Summary_Recife.txt',
	skiprows = 1, usecols = (range(2,18)))
#  0        1            2          3        4        5         6        7            8                 9     10     11           12       13      14              15  
#Year/Julian Date/Zero Crossings/Ave. Ht./Ave. Per./Max Ht./Sig. Wave/Sig. Per./Peak Per.(Tp)/Peak Per.(READ)/HM0/Mean Theta/Sigma Theta/ H1/10 / T.H1/10	/Mean Per.(Tz)

ax_data = loadtxt('/home/hppp/Dropbox/Tese/PNBOIA_Processamento/HNE/Recife_HNE/Summary_Recife.txt',
	dtype = str, skiprows = 1, usecols = (0,1))

#Saida site (baixado em 08/09/2013)
site = loadtxt('/home/hppp/Dropbox/Tese/PNBOIA_Processamento/HNE/Recife_HNE/pnboia.B69154_argos.dat',
	delimiter=',', skiprows = 1, usecols = (2,3,4,5,6,45,46,47,48))
#  0   1   2   3     4    5    6   7   8
# ano mes dia hora minuto Hs Hmax Tp Dirm

#melhorar formad e carregar os dados. ver uma forma de ler apenas a primeira coluna como string, ou ja separar a primeira coluna
# por '/' e a segunda por ':'.

#obs: deixa o minuto como '00'

#deixa os valores com -99999 (erro) com nan

site1 = copy(site)

for i in range(site.shape[1]):

	site[find(site[:,i] == -99999),i] = nan



# Cria numeros inteiros com as datas

#Python

#ano
ano_py = py[:,0]

#mes
mes_py = py[:,1]

#dia
dia_py = py[:,2]

#hora
hora_py = py[:,3]

#minuto
min_py = py[:,4]


#Axys - Summary

#ano
ano_ax = [int(ax_data[i,0][0:4]) for i in range(len(ax_data))]

#mes
mes_ax = [int(ax_data[i,0][5:7]) for i in range(len(ax_data))]

#dia
dia_ax = [int(ax_data[i,0][8:10]) for i in range(len(ax_data))]

#hora
hora_ax = [int(ax_data[i,1][:2]) for i in range(len(ax_data))]

#minuto
min_ax = [int(ax_data[i,1][3:]) for i in range(len(ax_data))]

#Site

#ano
ano_st = site[:,0]

#mes
mes_st = site[:,1]

#dia
dia_st = site[:,2]

#hora
hora_st = site[:,3] 

#minuto (deixa o minuto como zero)
min_st = zeros(len(site))


#cria variaveis de data com funcao datetime

#Axys

datam_ax = []

for i in range(len(ax_data)):

	datam_ax.append(datetime(ano_ax[i],mes_ax[i],dia_ax[i],hora_ax[i],min_ax[i]))

#deixa em ordem crescente (nao eh necessario)
datam_ax_sort = sort(datam_ax)

#Python

datam_py = []

for i in range(len(py)):

	datam_py.append(datetime(int(ano_py[i]),int(mes_py[i]),int(dia_py[i]),int(hora_py[i]),int(min_py[i])))

#Site

datam_st = []

for i in range(len(site)):

	datam_st.append(datetime(int(ano_st[i]),int(mes_st[i]),int(dia_st[i]),int(hora_st[i]),int(min_st[i])))


#Definicao de parametros de onda

#Definicao de parametros de onda

#python
hm0_py = py[:,11]
tp_py = py[:,12]
tmed_py = py[:,8]
thmax_py = py[:,9]
dirtp_py = py[:,13]
hmax_py = py[:,7]
hs_py = py[:,5]
h10_py = py[:,6]

#axys
hm0_ax = ax[:,10]
tp_ax = ax[:,8] #qual periodo usar?
tmed_ax = ax[:,15]
th10_ax = ax[:,14]
dirtp_ax = ax[:,11]
hmax_ax = ax[:,5]
hs_ax = ax[:,6]
h10_ax = ax[:,13]

#site
hs_st = site[:,5]
hmax_st = site[:,6]
tp_st = site[:,7]
dirm_st = site[:,8]


##correcao dos dados (para facilitar na visualizacao dos graficos
# pois tem valores de hs de 1200 no site)

# hs_st[(find(hs_st>30))] = nan



#Graficos

#hm0 
# figure()
# plot_date(datam_py,hm0_py,'bo')
# plot_date(datam_ax,hm0_ax,'go',alpha=0.5)
# title('Hm0 - Recife')
# ylabel('metros')
# legend(('python','axys'))

#hs
figure()
plot_date(datam_py,hs_py,'bo')
plot_date(datam_ax,hs_ax,'go',alpha=0.6)
plot_date(datam_st,hs_st,'ro',alpha=0.5)
title('Hs - Recife')
ylabel('metros')
legend(('python','axys','site'))

#h 1/10
# figure()
# plot_date(datam_py,h10_py,'bo')
# plot_date(datam_ax,h10_ax,'go',alpha=0.5)
# title('H 1/10 - Recife')
# ylabel('metros')
# legend(('python','axys'))

#hmax
# figure()
# plot_date(datam_py,hmax_py,'bo')
# plot_date(datam_ax,hmax_ax,'go',alpha=0.6)
# plot_date(datam_st,hmax_st,'ro',alpha=0.5)
# ylabel('metros')
# title('Hmax - Recife')
# legend(('python','axys','site'))

#tp
figure()
plot_date(datam_py,tp_py,'bo')
plot_date(datam_ax,tp_ax,'go',alpha=0.6)
plot_date(datam_st,tp_st,'ro',alpha=0.5)
ylabel('segundos')
title('Tp - Recife')
legend(('python','axys','site'))

#tmed
# figure()
# plot_date(datam_py,tmed_py,'bo')
# plot_date(datam_ax,tmed_ax,'go',alpha=0.5)
# title('tmed')
# legend(('python','axys'))

#t hmax
# figure()
# plot_date(datam_py,thmax_py,'bo')
# plot_date(datam_ax,th10_ax,'go',alpha=0.6)
# title('t hmax')
# legend(('python','axys'))

#dirtp
figure()
plot_date(datam_py,dirtp_py,'bo')
plot_date(datam_ax,dirtp_ax,'go',alpha=0.6)
plot_date(datam_st,dirm_st,'ro',alpha=0.5)
title('Dirtp - Recife')
ylabel('graus')
legend(('python','axys','site'))





show()