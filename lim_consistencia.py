#Cria limites para utilizar em testes de controle de qualidade de dados
#em boias meteo-oceanograficas
#
#1) Cria limite para teste de gradiente. 
#Descricao: Aproximacao da primeira e segunda derivada em series consistentes,
#e fazer um histograma desses dados para verificar variacoes normais para t e t-1
#
#2) Cria limites de spikes para as diversas series
#
#3) Verificar limites toleraveis para erros nas series, em funcao de um limite
#de erro, como RMS

from numpy import *
from pylab import *
from datetime import datetime

# ================================================================================== #
#Carrega dados da boia minuano pre-processados (saida_minuano.txt)
dados_minuano = loadtxt('C:\Users\hppp\Dropbox\Tese\CQ_Python\Processamento\Rotinas\Rotinas_MINUANO\saida_minuano.txt')

#cria data para arquivo pre-processado 
datam = []
for i in range(len(dados_minuano)):
    
    datam.append(datetime(int(dados_minuano[i,0]),int(dados_minuano[i,1]),int(dados_minuano[i,2]),int(dados_minuano[i,3])))

datam = array(datam)
# ================================================================================== #
#Definicao das variaveis
[at,rh,ws1,ws2,wg1,wg2,wd1,wd2,wt,bp,sigw,sigp,maxw,sr] = [dados_minuano[:,4],dados_minuano[:,5],dados_minuano[:,6],
dados_minuano[:,7],dados_minuano[:,8],dados_minuano[:,9],dados_minuano[:,10],dados_minuano[:,11],dados_minuano[:,12],
dados_minuano[:,13],dados_minuano[:,14],dados_minuano[:,15],dados_minuano[:,16],dados_minuano[:,17]]

# ================================================================================== #
### LIMITE PARA TESTE DE GRADIENTE ###

#primeira derivada (lag = 1)
#d1 =  
#    
#    deriv1 = diff(vet1)    
#    deriv11 = diff(deriv1)
#    
#    deriv2 = diff(vet2)
#    deriv22 = diff(deriv2)
#    
#    der1 = concatenate((deriv1,deriv2))
#    der2 = concatenate((deriv11,deriv22))
#    
#    return der1, der2