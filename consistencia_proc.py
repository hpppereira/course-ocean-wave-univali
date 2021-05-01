# -*- coding: utf-8 -*-
#
#Consistencia de parametros meteo-oceanograficos processados
#
#Autor: Henrique P. P. Pereira
#
#Data da ultima modificacao: 25/10/2013
#Obs: Por enquanto adaptado para os dados da boia MINUANO - RS
# 
#Funcoes: 'range' - teste de range
#         'spike' - teste de spikes (em contrucao)
# .... fazer aqui todos os testes para os dados processados


# ================================================================================== #
#importa bibliotecas

from numpy import *

# ================================================================================== #

def faixa(vet,linf,lsup,flag):
    
    '''
    
    TESTE DE FAIXA (RANGE)
    
    Dados de entrada: var - variavel
                      linf - limite inferior
                      lsup - limite superior
    
    Dados de saida: var1 - variavel consistente (com NaN no lugar do dado espúrio)
                    flag - parametro + flag
       
    Obs: A saida 'flag' cria uma lista com o valor do parametro e o flag
         O flag utilizado para o teste de range eh: '1'
         Dados 'consistentes' recebem flag = '0'
    
    '''
    
    #Inicializacao da rotina
    
    var1 = copy(vet)

    for i in range(len(vet)):
        
        #temperatura do ar
        if vet[i] < linf or vet[i] > lsup:
            
            #cria uma lista com o valor e o flag recebido
            #flag.append('1')
            flag[i] = flag[i]+'1'
            
            #o valor do dado inconsistente recebe 'nan'
            var1[i] = nan
            
        else:
            
            #flag.append('0')
            flag[i] = flag[i]+'0'
    
    return var1,flag
    
# ================================================================================== #
    
def spike(vet,linf,lsup,flag):
    
    '''
    
    TESTE DE SPIKE
    
    Dados de entrada: var - variavel
                      linf - limite inferior
                      lsup - limite superior
    
    Dados de saida: var1 - variavel consistente (com NaN no lugar do dado espúrio)
                    flag - parametro + flag
       
    Obs: A saida 'flag' cria uma lista com o valor do parametro e o flag
         O flag utilizado para o teste de range eh: '1'
         Dados 'consistentes' recebem flag = '0'
    
    '''
    
    #Inicializacao da rotina
    
    var1 = copy(vet)

    for i in range(len(vet)):
        
        #temperatura do ar
        if vet[i] < linf or vet[i] > lsup:
            
            flag[i] = flag[i]+'1'
            
            #o valor do dado inconsistente recebe 'nan'
            var1[i] = nan
            
        else:
            
            #flag[i] = [vet[i],'0']
            flag[i] = flag[i]+'0'
            
    return var1,flag
    
# ================================================================================== #

def gradiente(vet,lag,lim,flag):
    
    '''
    
    TESTE DE GRADIENTE
    
    Dados de entrada: var - variavel
                      lag - delta tempo para o teste (horas: 0 - 3)
                      lim - variacao maxima (para o lag escolhido)
    
    Dados de saida: var1 - variavel consistente (com NaN no lugar do dado espúrio)
                    flag - parametro + flag
       
    Obs: A saida 'flag' cria uma lista com o valor do parametro e o flag
         O flag utilizado para o teste de range eh: '1'
         Dados 'consistentes' recebem flag = '0'
    
    '''
    
    #Inicializacao da rotina
    
    var1 = copy(vet)
    
    #calcula a derivada de acordo com o lag (horas)
    a = vet[lag:] - vet[:-lag]
    
    for i in range(len(a)):
                        
        if a[i] > lim or a[i] < -lim:
            
            flag[i] = flag[i]+'1'
            
            #o valor do dado inconsistente recebe 'nan'
            var1[i] = nan
            
        else:
            
            flag[i] = flag[i]+'0'
            
    #flag[i+1] = flag[i+1]+'0'
                
    return var1,flag
    
    
# ================================================================================== #

def gradiente_ndbc(vet,lag,dp_var,flag):
    
    '''
    
    TESTE DE GRADIENTE
    
    Dados de entrada: var - variavel
                      lag - delta tempo para o teste (horas: 0 - 3)
                      dp_var - desvio padrão escolhido para a variavel
    
    Dados de saida: var1 - variavel consistente (com NaN no lugar do dado espúrio)
                    flag - parametro + flag
                    lim - limite calculado pela formula
       
    Obs: A saida 'flag' cria uma lista com o valor do parametro e o flag
         O flag utilizado para o teste de range eh: '1'
         Dados 'consistentes' recebem flag = '0'
    
    '''
    
    #Inicializacao da rotina
    
    var1 = copy(vet)
    
    #cria limite de acordo com a formula da ndbc 09
    lim = 0.56 * dp_var * sqrt(lag)
    
    #calcula a derivada de acordo com o lag (horas)
    a = vet[lag:] - vet[:-lag]
    
    for i in range(len(a)):
                        
        if a[i] > lim or a[i] < -lim:
            
            flag[i] = flag[i]+'1'
            
            #o valor do dado inconsistente recebe 'nan'
            var1[i] = nan
            
        else:
            
            flag[i] = flag[i]+'0'
            
    #flag[i+1] = flag[i+1]+'0'
                
    return var1,flag,lim
    