# -*- coding: utf-8 -*-

#carrega os arquivos da boia MINUANO - RS
#
# Desenvolvido por: Henrique P. P. Pereira - heniqueppp@oceanica.ufrj.br
#
# Data da ultima modificacao: 22/10/2013
#
# ================================================================================== #
# Funcao 'lista_minuano': Cria uma lista com o nome dos arquivos com extensao .CSV que estao
# dentro do diretorio 'pathname' indicado.
#
# Funcao 'dados_hne': Atribui os dados dos arquivos a variavel 'data' com o tempo, e 
# 'dados' com elevacao e deslocamentos norte e leste 
#
# ================================================================================== #

# ================================================================================== #
##Importa bibliocas utilizadas

from numpy import * 	#modulo para trabalhar com matrizes
import glob				#modulo que lista os arquivos de um diretorio

#======================================================================#

#Entrada: pathname - diretorio que estao os arquivos
#
#Saida: arq - variavel com o nome dos arquivos

def lista_csv(pathname):

	''' Lista arquivos com extensao .CSV 
	que estao dentro do diretorio 'pathname' '''

	#lista de arquivos (acha os arquivos com a extensao HNE que estao dentro da pasta)
	filelist = glob.glob(pathname + "*CSV")

	#coloca os arquivos em ordem
	filelist = sort(filelist)

	lista = []

	for f in filelist:

		lista.append(f[-10:])

	return lista

#======================================================================#

#carrega arquivos da boia minuano 1


def dados_csv(pathname,lista):
    
#          0      1    2   3  4   5   6   7   8   9  10 11  12   13   14  15
#dados = data,hora_min,at,rh,ws1,ws2,wg1,wg2,wd1,wd2,wt,bp,sigw,sigp,maxw,sr
    
    dados = zeros((1,16))
    
    for i in range(len(lista)):
        
       dados1 = loadtxt(pathname + lista[i],
            skiprows=0,delimiter=',',usecols=(0,1,5,6,7,8,9,10,11,12,14,15,16,17,18,19),unpack=False)
       
       dados = concatenate((dados,dados1))
       
    dados = dados[1:,:]
        
    return dados