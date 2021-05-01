# -*- coding: utf-8 -*-
# Aula 1 - Python

#Henrique P. P. Pereira

## Rotina em permanente construcao

#Observacoes: para ter acento no texto, tem que ter escrito

##==========================================================================================##

##site do Rafael Sotelino com informacoes sobre o python e pacotes de instalacao
##curso ministrado pelo ieapm
##http://www.rsoutelino.com/rsoutelino/default/formpython

##Informacoes do site:
##Editor de texto para desenvolvimento de codigo. sugerimos SublimeText2
##Python 2.7
##iPython mais recente 
##Modulos e bibliotecas Python: Scipy, Matplotlib, Basemap toolkit do Matplotlib, netCDF4, Seawater e Pydap

##Instalacao em sistema operacional Debian/Ubuntu Linux via apt-get

##Neste caso, todos os pacotes sao baixados e compilados para o seu sistema em particular,
##ocupando menos espaco e com performance ligeiramente melhor. Segue as instrucoes abaixo:

##sudo apt-get install build-essential gfortran nco libnetcdf-dev libhdf5-serial libhdf5-serial-dev libkernlib1-gfortran netcdf-bin hdf5-tools
  
##Instalar o netcdf mais recente para sua arquitetura.
##http://www.unidata.ucar.edu/software/netcdf/

##sudo apt-get install python-scipy python-matplotlib python-mpltoolkits.basemap ipython python-pip python-setuptools python-wxtools python-wxversion python-netcdf

##sudo easy_install seawater pydap wx netcdf4


##==========================================================================================##


##para abrir o python no ipython utilizando o modulo pylab
##ipython --pylab 

##rodar um script, ex:
##run Aula_1_Python.py

##como carrega um arquivo texto (utiliza o numpy)
##dados = loadtxt('/home/henrique/Dropbox/Curso_Python_AD/ondas.txt')


##==========================================================================================##

#importa bibliotecas (ver funcoes na internet)
import numpy as np #chama o modulo numpy como np
from numpy import * #importa tudo do numpy - bom para trabalhar com matrizes
from scipy import * #modulo de biblioteca cientifica
from pylab import * #modulo parecido com o matlab 
import matplotlib #graficos
from datetime import * #graficos com eixos de datas


##==========================================================================================##


a = 1/2 #numero inteiro - funcao 'int'

a1 = 'string'

b = 1./2 # funcao float

#listas
c = [1,2,3,4,5,6]

##ver o tipo da variavel
## type(variavel)


#funcao 'append' utilizada para listas

#matriz vazia
d = []

for i in range(10): #funcao range, ou arange - util: 'for i in range(len(x)):' (equivalente matlab: 'for i = 1:len(x)')

	d.append(i)


#transforma lista 'e' em array

e = array(d)

#criar matriz 
x = np.array([[1,2,3],[1,2,3]])

##verifica dimensao de 'e'
##e.shape

#rearranja o array - util colocar uma dimensao lin,col
f = resize(e,(len(e),1))

#selecionar um elemento do array
g1 = f[0]
g2 = f[3]
g3 = f[0:-2]

h = resize(e,(len(e)/2,2))

i1 = h[1,1]

##funcao de imprimir
print i1

#concatenar uma string
frase = 'Isso' + ' e' + ' uma string'

#regua	
regua = '=' * 80

palavra = 'sem falta'
valor = 500

# %i = valor inteiro
print 'Precisamos de R$%i !!!' %valor

# %0.2f = 2 casa decimais de um float / %s = string
print 'Precisamos de R$%0.2f, %s !!!' %(valor,palavra)


#Lisas e tuplas

lista_vazia = []
lista_de_compras = ['alface', 'tomate' , 'banana']

lista_de_compras[0]

lista_de_compras[:2] #ate o elemento 2

lista_de_compras[2:] #do segundo em diante

lista_de_compras[-1] #o ultimo elemento

lista_de_compras[0:3:2]	


lista_dentro_de_listas = [[1,2,3],[1,2,3]]



#tuplas sao listas imutaveis

j = (32,5,3,8)

j1 = j[2]

#Dicionarios - palavra-chave: valor
#atribui uma palavra chave para cada conjunto de dados
vazio = {}

compras = {'salada' : ['alface', 'tomate', 'cebola'],
			'frutas' : ['melao', 'maca', 'laranja']}

#chamando as funcoes do dicionario
k1 = compras['salada'][1] #pega o segundo valor das 'saladas' que estao dentro das 'compras'
k2 = compras['frutas'] #pega todos os valores de frutas

compras['frutas'][2] = 'pessego' #coloca valores no dicionario

##deleta variavel
##del variavel

##deleta todas as variaveis
##reset

''' comentario 
em varias 
linhas '''

#Quebra de linha
'''string com quebra \n
de linha '''

#exec, equivale ao eval no matlab
#atribui nome de variaveis em forma dinamica

##mostra submodulos
##dir()

##ver variaveis
#whos

##help no ipython
##matplotlib?

##identacao, utilizar 4 espacos

##'for' utilizando 'continue' e 'break'
##continue, pula o valor e continua fazendo o loop
##break, para de executar e para o loop

#definindo funcoes

def potencia(a,b):
	l = a**b

	return l

#chama funcao
l = potencia(2,2)


##modulo e funcao - nome do arquivo = matematica , nome da funcao(def) = potencia
##l = matematica.potencia(2,2)

##utiliza valor por default
# def potencia(a,b=0):


##caso o usuario nao entre com o valor de b utiliza se b=0

#funcao pass, utilizado dentro do else

#verificar se um valor esta em uma lista

for n in [0,1,2,3,4,5]:

	if n in [1,2,3]:

		print 'alguma coisa'


##metodos dos objetos
##a='b'
##a. da um tab

##funcoes com valores e listas
##.append() - acrescenta valor

##.extend() - acrescenta 

#range - cria lista

##np.ones(30 5 14) - cria matriz de 3 dimensoes

##size = tamanho total da matriz

#tirar media da linha ou coluna

## x.mean() - faz  a media total
## x.mean(axis=0) - media da coluna
## x.mean(axis=1) - media da linha

o=np.arange(10,190,10)

p=np.linspace(1,10,20)

##plot simples
# plot(p)
# title('introducao python')
# xlabel('tempo')
# ylabel('parametro')
# axis('tight') #ajusta os eixos

##mostra figura
# show()

#data de hoje com funcao date
data = date.today()

#acha os indices
q = where(p>3)

#transformar um array em uma matriz de uma coluna

x1 = x.ravel()

##salvar figura no pyplot

##savefig('figura.jpg')

##f.readline #cada vez que roda, le uma linha


##==========================================================================================##


##exemplo

#import glob #lista os arquivos que tem em uma pasta

# pathname = '/Users/rsoutelino/'
# filelist = glob.glob(pathname + "*.cnv") #lista os arquvos que tem .cnv

# lon, lat, temp = [], [], []
# intervalo = 1000

# for file in filelist:

# 	f = open(file)
# 	lines = f.readlines()

# 	for k in range(len(lines)): #vai lendo um arquivo de cada vez para ser processado
# 			.
# 			.
# 			.
# 			.
# 			.

#observacoes

# para dar um tab em um bloco do script, selecionar
# o bloco e dar tab. para fazer o contrario, dar shft+tab



#### curso_aula4 - IEAPM ####

# import datetime as dt

# dt.timedelta #intervalo de tempo, em dias


# hoje = dt.date.today()

# agora = dt.datetime.now()

# amanha = hoje + dt.timedelta(1)

# import os #operacoes com o sistema operacional

# ! #serve para executar diretamente no shell

# !touch #cria arquivo no shell

# import sys

# sys.path #onde encontra os programas

# sys.platform


# #um metodo eh uma funcao dentro de uma classe
# e uma classe pode estar dentro de um modulo

# para criar a sintaxe de classe, escrever class e dar tab

# classes tem metodos e atributo, o atributo pode ser outra classe


# class ClassName(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, arg):
# 		super(ClassName, self).__init__()
# 		self.arg = arg
		
# uma docstring pode ser acessada por:
# ClassName?

# Lidando com erro

# def dividir(a,b):
# 	try:
# 		c = a/b
# 		return c
# 	except ZeroDivisionError:
# 		print "Divisao por zero nao existe"
# 	except TypeError
# 		print "Nao eh possivel divisao com strings"


# #funcao lamba
# serve para criar funcoes
# Ex: quadrado = lambda x: x ** 2

# import re
# serve para selecionar os dados que vc quer em 
# uma linha estranha

# plt.close('all')
