# -*- coding: utf-8 -*-

#Processamento dos dados meteorologicos da boia
#minuano, no rio grande do sul

# ================================================================================== #
#Importa bibliotecas

from numpy import *
from pylab import *
import consistencia_proc
import lim_consistencia
import graficos_minuano
import carrega_minuano
import data_minuano
from datetime import datetime

close('all')


# ================================================================================== #
#Carrega dados da boia minuano pre-processados (saida_minuano.txt)
dados_minuano = loadtxt('C:\Users\hppp\Dropbox\Tese\CQ_Python\Processamento\Rotinas\Rotinas_MINUANO\saida_minuano.txt')

#cria data para arquivo pre-processado 
datam = []
for i in range(len(dados_minuano)):
    
    datam.append(datetime(int(dados_minuano[i,0]),int(dados_minuano[i,1]),int(dados_minuano[i,2]),int(dados_minuano[i,3])))


# ================================================================================== #
#Carrega dados processados pelo ricardo

#ric = loadtxt('C:/Users/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Boia_MINUANO/saida_minuano_ricardo.txt',skiprows=1)
#
##       0    1     2    3     4      5   6   7
##ric = ano, mes, dia, hora, minuto, Hs, Tp, Hmax 
#
##cria data para os dados do ricardo
#data_ric = []
#for i in range(len(ric)):
#    
#    data_ric.append(datetime(int(ric[i,0]),int(ric[i,1]),int(ric[i,2]),int(ric[i,3]),int(ric[i,4])))
    

# ================================================================================== #
#Carrega os dados meteorologicos

#caminho com o nome dos arquivos da boia minuano (Windows)
#pathname1 = 'C:/Users/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Boia_MINUANO/1_Dados_da_Minuano_de_240502_a_130104/'
#pathname2 = 'C:/Users/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Boia_MINUANO/2_Dados_da_Minuano_de_220104_a_171004/'
#pathname3 = 'C:/Users/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Boia_MINUANO/3_Dados_da_Minuano_de_040707_a_130508/'
#pathname4 = 'C:/Users/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Boia_MINUANO/4_Dados_da_Minuano_de_130508_a_280410/'
#pathname5 = 'C:/Users/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Boia_MINUANO/2007_2008/'

#caminho com o nome dos arquivos da boia minuano (Ubuntu)
#pathname1 = '/home/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Boia_MINUANO/1_Dados_da_Minuano_de_240502_a_130104/'
#pathname2 = '/home/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Boia_MINUANO/2_Dados_da_Minuano_de_220104_a_171004/'
#pathname3 = '/home/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Boia_MINUANO/3_Dados_da_Minuano_de_040707_a_130508/'
#pathname4 = '/home/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Boia_MINUANO/4_Dados_da_Minuano_de_130508_a_280410/'
#pathname5 = '/home/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Boia_MINUANO/2007_2008/'


# ================================================================================== #
#Lista arquivos .CSV que estao dentro do diretorio 'pathname'

##cria lista com o nome dos arquivos
#lista1 = carrega_minuano.lista_csv(pathname1)
#lista2 = carrega_minuano.lista_csv(pathname2)
#lista3 = carrega_minuano.lista_csv(pathname3)
#lista4 = carrega_minuano.lista_csv(pathname4)
#lista5 = carrega_minuano.lista_csv(pathname5)
#
##chama funcao para carregar arquivos da boia minuano 
#dados_minuano1 = carrega_minuano.dados_csv(pathname1,lista1)
#dados_minuano2 = carrega_minuano.dados_csv(pathname2,lista2)
#dados_minuano3 = carrega_minuano.dados_csv(pathname3,lista3)
#dados_minuano4 = carrega_minuano.dados_csv(pathname4,lista4)
#dados_minuano5 = carrega_minuano.dados_csv(pathname5,lista5)
#
##                  0      1    2   3  4   5   6   7   8   9  10 11  12   13   14  15
##dados_minuano = data,hora_min,at,rh,ws1,ws2,wg1,wg2,wd1,wd2,wt,bp,sigw,sigp,maxw,sr
#dados_minuano = concatenate((dados_minuano1,dados_minuano2,dados_minuano3,dados_minuano4,dados_minuano5))


# ================================================================================== #
#Chama funcao para criar data (utiliza funcao 'datetime')

#datam,ano,mes,dia,hora,minuto = data_minuano.data(dados_minuano)


# ================================================================================== #
# Deixa a matriz 'dados_minuano' em ordem crescente

##acha os indices para ordem crescente
#datam_aux = argsort(datam)
#
##deixa a data em ordem crescente
#datam = array(datam)[datam_aux]
#
##matriz de data em ordem crescente
#ano = array(ano)[datam_aux]
#mes = array(mes)[datam_aux]
#dia = array(dia)[datam_aux]
#hora = array(hora)[datam_aux]
#
#data = array([ano,mes,dia,hora]).T
#
##deixa os dados em ordem crescente
#dados_minuano = concatenate((data,dados_minuano[datam_aux,:]),axis=1)
#dados_minuano = dados_minuano[:,[0,1,2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]

##                  0  1    2   3    4       5     6  7  8   9   10  11 12  13  14 15  16   17   18  19   
##dados_minuano = ano,mes,dia,hora,data,data_hora,at,rh,ws1,ws2,wg1,wg2,wd1,wd2,wt,bp,sigw,sigp,maxw,sr


# ================================================================================== #
#Definicao das variaveis
[at,rh,ws1,ws2,wg1,wg2,wd1,wd2,wt,bp,sigw,sigp,maxw,sr] = [dados_minuano[:,4],dados_minuano[:,5],dados_minuano[:,6],
dados_minuano[:,7],dados_minuano[:,8],dados_minuano[:,9],dados_minuano[:,10],dados_minuano[:,11],dados_minuano[:,12],
dados_minuano[:,13],dados_minuano[:,14],dados_minuano[:,15],dados_minuano[:,16],dados_minuano[:,17]]


# ================================================================================== #
#Verifica os limites para o controle de qualidade

#der1, der2 = lim_consistencia.lim_grad(at[0:6177],at[27731:41810])


# ================================================================================== #
#Definicao das variaveis para o Controle de Qualidade
# variavel_consistente (var_c) ; vetor_de_flags (var_flag)

at_c = copy(at) ; at_flag = ['' for x in range(len(at))]
rh_c = copy(rh) ; rh_flag = ['' for x in range(len(rh))]
ws1_c = copy(ws1) ; ws1_flag = ['' for x in range(len(ws1))]
ws2_c = copy(ws2) ; ws2_flag = ['' for x in range(len(ws2))]
wg1_c = copy(wg1) ; wg1_flag = ['' for x in range(len(wg1))]
wg2_c = copy(wg2) ; wg2_flag = ['' for x in range(len(wg2))]
wd1_c = copy(wd1) ; wd1_flag = ['' for x in range(len(wd1))]
wd2_c = copy(wd2) ; wd2_flag = ['' for x in range(len(wd2))]
wt_c = copy(wt) ; wt_flag = ['' for x in range(len(wt))]
bp_c = copy(bp) ; bp_flag = ['' for x in range(len(bp))]
sigw_c = copy(sigw) ; sigw_flag = ['' for x in range(len(sigw))]
sigp_c = copy(sigw) ; sigp_flag = ['' for x in range(len(sigp))]
maxw_c = copy(maxw) ; maxw_flag = ['' for x in range(len(maxw))]
sr_c = copy(sr) ; sr_flag = ['' for x in range(len(sr))]


# ================================================================================== #
#Testes de Controle de Qualidade


### TESTE DE FAIXA (RANGE) ###

#Ex: var_c, var_flag = consistencia_proc.faixa(var,linf,lsup,flag)

#at_c,at_flag = consistencia_proc.faixa(at_c,-40,60,at_flag)
#rh_c,rh_flag = consistencia_proc.faixa(rh,0,100,rh_flag)
#ws1_c,ws1_flag = consistencia_proc.faixa(ws1,0,62,ws1_flag)
#ws2_c,ws2_flag = consistencia_proc.faixa(ws2,0,62,ws2_flag)
#wg1_c,wg1_flag = consistencia_proc.faixa(wg1,0,82,wg1_flag)
#wg2_c,wg2_flag = consistencia_proc.faixa(wg2,0,82,wg2_flag)
#wd1_c,wd1_flag = consistencia_proc.faixa(wd1,0,360,wd1_flag)
#wd2_c,wd2_flag = consistencia_proc.faixa(wd2,0,360,wd2_flag)
#wt_c,wt_flag = consistencia_proc.faixa(wt,-5,40,wt_flag)
#bp_c,bp_flag = consistencia_proc.faixa(bp,600,1100,bp_flag)
#sigw_c,sigw_flag = consistencia_proc.faixa(sigw,0,35,sigw_flag)
#sigp_c,sigp_flag = consistencia_proc.faixa(sigp,0,30,sigp_flag)
#maxw_c,maxw_flag = consistencia_proc.faixa(maxw,0,35,maxw_flag)
#sr_c,sr_flag = consistencia_proc.faixa(sr,0,2150,sr_flag)


### TESTE DE SPIKE ###

#Ex: var_c, var_flag = consistencia_proc.faixa(var,linf,lsup,flag)

#at_c,at_flag = consistencia_proc.spike(at_c,0,35,at_flag)
#rh_c,rh_flag = consistencia_proc.spike(rh,0,100,rh_flag)
#ws1_c,ws1_flag = consistencia_proc.spike(ws1,0,30,ws1_flag)
#ws2_c,ws2_flag = consistencia_proc.spike(ws2,0,30,ws2_flag)
#wg1_c,wg1_flag = consistencia_proc.spike(wg1,0,40,wg1_flag)
#wg2_c,wg2_flag = consistencia_proc.spike(wg2,0,40,wg2_flag)
#wd1_c,wd1_flag = consistencia_proc.spike(wd1,0,360,wd1_flag)
#wd2_c,wd2_flag = consistencia_proc.spike(wd2,0,360,wd2_flag)
#wt_c,wt_flag = consistencia_proc.spike(wt,0,35,wt_flag)
#bp_c,bp_flag = consistencia_proc.spike(bp,950,1050,bp_flag)
#sigw_c,sigw_flag = consistencia_proc.spike(sigw,0,16,sigw_flag)
#sigp_c,sigp_flag = consistencia_proc.spike(sigp,0,30,sigp_flag)
#maxw_c,maxw_flag = consistencia_proc.spike(maxw,0,35,maxw_flag)
#sr_c,sr_flag = consistencia_proc.spike(sr,0,2150,sr_flag)


### TESTE DE GRADIENTE ###

#Ex: var_c, var_flag = consistencia_proc.gradiente(at_c,lag,lim,flag)
#Obs: O lag em horas por enquanto soh esta de 1 hora (primeira derivada)

#at_c, at_flag = consistencia_proc.gradiente(at_c,3,1,at_flag)
#rh_c,rh_flag = consistencia_proc.gradiente(rh,3,1,rh_flag)
#ws1_c,ws1_flag = consistencia_proc.gradiente(ws1,3,1,ws1_flag)
#ws2_c,ws2_flag = consistencia_proc.gradiente(ws2,3,1,ws2_flag)
#wg1_c,wg1_flag = consistencia_proc.gradiente(wg1,3,1,wg1_flag)
#wg2_c,wg2_flag = consistencia_proc.gradiente(wg2,3,1,wg2_flag)
#wd1_c,wd1_flag = consistencia_proc.gradiente(wd1,3,45,wd1_flag)
#wd2_c,wd2_flag = consistencia_proc.gradiente(wd2,3,45,wd2_flag)
#wt_c,wt_flag = consistencia_proc.gradiente(wt,3,1,wt_flag)
#bp_c,bp_flag = consistencia_proc.gradiente(bp,3,5,bp_flag)
#sigw_c,sigw_flag = consistencia_proc.gradiente(sigw,3,2,sigw_flag)
#sigp_c,sigp_flag = consistencia_proc.gradiente(sigp,3,5,sigp_flag)
#maxw_c,maxw_flag = consistencia_proc.gradiente(maxw,3,15,maxw_flag)
#sr_c,sr_flag = consistencia_proc.gradiente(sr,3,2150,sr_flag) #nao faz nada , flag=0

### TESTE DE GRADIENTE DA NDBC ###

#Ex: var_c, var_flag,var_limg = consistencia_proc.gradiente(at_c,lag,DP_VAR,flag)
#Obs: So eh realizado para as variaveis: bp, at, wt, ws1, ws2, sigw, sigp, rh

at_c, at_flag,at_limg = consistencia_proc.gradiente_ndbc(at_c,3,4,at_flag)
rh_c,rh_flag,rh_limg = consistencia_proc.gradiente_ndbc(rh,3,12,rh_flag)
ws1_c,ws1_flag,ws1_limg = consistencia_proc.gradiente_ndbc(ws1,3,4,ws1_flag)
ws2_c,ws2_flag,ws2_limg = consistencia_proc.gradiente_ndbc(ws2,3,4,ws2_flag)
wt_c,wt_flag,wt_limg = consistencia_proc.gradiente_ndbc(wt,3,4,wt_flag)
bp_c,bp_flag,bp_limg = consistencia_proc.gradiente_ndbc(bp,3,6,bp_flag)
sigw_c,sigw_flag,sigw_limg = consistencia_proc.gradiente_ndbc(sigw,3,1,sigw_flag)
sigp_c,sigp_flag,sigp_limg = consistencia_proc.gradiente_ndbc(sigp,3,3,sigp_flag)

# ================================================================================== #
#Cria vetor de flags em array

at_flag = concatenate((at.reshape((len(at),1)),array(at_flag).reshape((len(at_flag),1))),axis=1)
rh_flag = concatenate((rh.reshape((len(rh),1)),array(rh_flag).reshape((len(rh_flag),1))),axis=1)
ws1_flag = concatenate((ws1.reshape((len(ws1),1)),array(ws1_flag).reshape((len(ws1_flag),1))),axis=1)
ws2_flag = concatenate((ws2.reshape((len(ws2),1)),array(ws2_flag).reshape((len(ws2_flag),1))),axis=1)
wg1_flag = concatenate((wg1.reshape((len(wg1),1)),array(wg1_flag).reshape((len(wg1_flag),1))),axis=1)
wg2_flag = concatenate((wg2.reshape((len(wg2),1)),array(wg2_flag).reshape((len(wg2_flag),1))),axis=1)
wd1_flag = concatenate((wd1.reshape((len(wd1),1)),array(wd1_flag).reshape((len(wd1_flag),1))),axis=1)
wd2_flag = concatenate((wd2.reshape((len(wd2),1)),array(wd2_flag).reshape((len(wd2_flag),1))),axis=1)
wt_flag = concatenate((wt.reshape((len(wt),1)),array(wt_flag).reshape((len(wt_flag),1))),axis=1)
bp_flag = concatenate((bp.reshape((len(bp),1)),array(bp_flag).reshape((len(bp_flag),1))),axis=1)
sigw_flag = concatenate((sigw.reshape((len(sigw),1)),array(sigw_flag).reshape((len(sigw_flag),1))),axis=1)
sigp_flag = concatenate((sigp.reshape((len(sigp),1)),array(sigp_flag).reshape((len(sigp_flag),1))),axis=1)
maxw_flag = concatenate((maxw.reshape((len(maxw),1)),array(maxw_flag).reshape((len(maxw_flag),1))),axis=1)
sr_flag = concatenate((sr.reshape((len(sr),1)),array(sr_flag).reshape((len(sr_flag),1))),axis=1)


# ================================================================================== #
#Graficos

#chama funcao para plotagem dos graficos
graficos_minuano.graficos(datam,at,at_c,rh,rh_c,ws1,ws1_c,ws2,ws2_c,wg1,wg1_c,
wg2,wg2_c,wd1,wd1_c,wd2,wd2_c,wt,wt_c,bp,bp_c,sigw,sigw_c,sigp,sigp_c,maxw,maxw_c,sr,sr_c)

#show()


# ================================================================================== #
#Outros/Temporarios

#figure()
#plot_date(data_ric,ric[:,5])
#plot_date(datam,sigw,'r*',alpha=0.3)
#title('temp ar - comparacao com dados ricardo')


# ================================================================================== #
#Tabela para salvar dados
#savetxt('saida_minuano.txt',dados_minuano,fmt='%5.2f')
