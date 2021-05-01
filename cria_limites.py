## Programa para criar limies de spikes dos dados brutos e processados
## 
## Dados: Boia Marinha - RS , no periodo de 2009-2011 com lacunas (maioria dos dados sao de 2009)
##
## Series analisadas:
## Bruto:
## heave, dspx, dspy dos arquivos .HNE
## 
## Processado:
## Hs, H10, Hmax, Tmed, THmax, HTmax, Hm0 Tp DirTp

#importa modulos
from numpy import *		#modulo para trabalhar com matrizes
from pylab import *	#importa funcao find
import carrega_axys 	#modulo de listar e atribuir valores dos dados
import proc_onda 		#modulo para processamento dos dados no tempo e frequencia
import consistencia_axys #modulo para realizar a consistencia de dados brutos e processados

# ================================================================================== #
## Lista arquivos .HNE

#caminho onde estao os arquivos .HNE
pathname = '/home/hppp/Dropbox/Tese/CQ_Python/Boia_MB_RS/'

#Lista arquivos .HNE que estao dentro do diretorio 'pathname'
#cria lista com o nome dos arquivos
lista = carrega_axys.lista_hne(pathname)

#escolhe a data inicial e final para ser analisada (opcional, mudar no 'for')
z0 = '200905011000'+'.HNE'
z1 = '200905020000'+'.HNE'

#acha o indice na variavel 'lista' dos arquivos escolhidos para serem analisados 
p0 = find(array(lista) == z0)
p1 = find(array(lista) == z1) + 1 #coloca +1 para pegar registro p1

#comprimento da serie temporal a ser processada (em potencia de 2)
numproc = 1024

# ================================================================================== #
##Lista de variaveis a serem criadas durante o programa

lista_arq = [] 			  #lista do nome dos arquivos que passaram pela consistencia
lista_inconsistente = []  #lista de arquivos inconsistentes (nao serao processados)
lista_consistente = []    #lista de arquivos consistentes (serao processados)
lista_flag = []			  #lista de flags dos arquivos que passaram pela consistencia (colocar data e hora)
mat_onda = []			  #matriz com os parametros de onda calculados = [Hs, H10, Hmax, Tmed, Tmax, THmax, HTmax, hm0, tp, dirtp]

eta_mat = zeros((1500,len(lista)))		# _mat - series temporais (cada coluna eh uma hora)
dspx_mat = zeros((1500,len(lista)))		# _mat_cons - matriz de dados com series temporais dos dados aprovados na consistencia
dspy_mat = zeros((1500,len(lista)))		# _mat_incons - matriz de dados com series temporais dos dados reprovados na consistencia 
eta_mat_cons = zeros((1500,len(lista)))    ## tem 1500 linhas para ser uma matriz maior que os dados da axys, que variam prox. a 1300
dspx_mat_cons = zeros((1500,len(lista)))   
dspy_mat_cons = zeros((1500,len(lista)))   
eta_mat_incons = zeros((1500,len(lista)))  
dspx_mat_incons = zeros((1500,len(lista)))  
dspy_mat_incons = zeros((1500,len(lista)))

#cria matriz com nan para nao confundir na plotagem com zeros no final caso o vetor seja menor que 1024 pontos
eta_mat[:,:] = nan    #tomar cuidado pois mascara o tamanho do vetor na funcao 'len'
dspx_mat[:,:] = nan
dspy_mat[:,:] = nan

eta_mat_cons[:,:] = nan  
dspx_mat_cons[:,:] = nan
dspy_mat_cons[:,:] = nan

eta_mat_incons[:,:] = nan
dspx_mat_incons[:,:] = nan
dspy_mat_incons[:,:] = nan

# ================================================================================== #
##Carrega os dados e cria 3 matrizes para heave, pitch e roll, em que cada coluna eh uma hora

#colunas do eta_mat (cada coluna eh uma hora)
jj = -1   #contador de arquivos inconsistentes
kk = -1   #contador de arquivos consistentes
cont = -1 #contador de arquivos analisados

for i in range(len(lista)):  #le todos os arquivos da lista
#for i in range(p0,p1):		  #le os arquivos escolhidos

	#contador de arquivos analisados
	cont = cont + 1
	
	#atribui o nome do arquivo a variavel 'arq'
	arq = lista[i]

	#cria variavel string do nome dos arquivos
	lista_arq.append(arq)

	#atribui as variaveis em 'dados' e a data em 'data'
	dados, data = carrega_axys.dados_hne(arq)

	#cria variaveis de data
	ano = int(data[0])
	mes = int(data[1])
	dia = int(data[2])
	hora = int(data[3])
	minuto = int(data[4])

	#define variaveis de onda (verificar as colunas dependendo do arquivo de entrada)
	t = dados[:,0]
	eta = dados[:,1]
	dspy = dados[:,2]
	dspx = dados[:,3]

	#coloca serie temporal em cada coluna (tanto os consistentes como os inconsistentes)
	eta_mat[0:len(eta),cont] = eta
	dspx_mat[0:len(dspx),cont] = dspx
	dspy_mat[0:len(dspy),cont] = dspy

	# ================================================================================== #
	## Faz a consistencia dos dados brutos para pegar somente dados aparentemente consistentes (sem erros grosseiros)	

	#importa modulo de consistencia e funcao da conistencia de dados brutos
	flag = consistencia_axys.consiste_bruto(t,eta,dspy,dspx,arq)

	# flag = '0' - passou na consistencia de dados brutos

	#Dados que receberem flags (flag diferente de '0') nao serao processados)
	#O dado ate poderia ser processado. mas provavelmente dara erro antes de 
	#processar todos os dados. Entao para o caso de consistencia em terra,
	#vale qualificar um flag nessas dados e depois processar os mesmos.

	#Se o flag for diferente de zero (quer dizer que recebeu flag)
	if flag <> '0': 

		#cria lista com o nome dos arquivos inconsisentes
		lista_inconsistente.append(int(arq[0:12]))

		#cria lista de flags de todos os arquivos
		lista_flag.append([ano, mes, dia, hora, minuto, flag])

		#cria matriz com series temporais reprovadas na consistencia
		jj = jj + 1 #contador de colunas (cada coluna eh uma hora)
		
		#coloca serie temporal em cada coluna (inconsistentes)
		eta_mat_incons[0:len(eta),jj] = eta
		dspx_mat_incons[0:len(dspx),jj] = dspx
		dspy_mat_incons[0:len(dspy),jj] = dspy
			
	#Dados consistentes (flag igual a '0') serao processados
	else: 

		#lista arquivos consistentes (nome do arquivo)
		lista_consistente.append(int(arq[0:12]))
		
		#comprime o comprimento dos vetores no tamanho de 'numproc'
		t = dados[0:numproc,0]
		eta = dados[0:numproc,1]
		dspy = dados[0:numproc,2]
		dspx = dados[0:numproc,3]

		# ================================================================================== #
		##cria matriz com series temporais aprovadas na consistencia
		
		kk = kk + 1 #contador de colunas (cada coluna eh uma hora)

		#coloca serie temporal em cada coluna (consistentes)
		eta_mat_cons[0:len(eta),kk] = eta
		dspx_mat_cons[0:len(dspx),kk] = dspx
		dspy_mat_cons[0:len(dspy),kk] = dspy


#series temporais (consistentes e inconsistentes)
eta_mat = eta_mat[0:len(eta),0:cont+1]
dspx_mat = dspx_mat[0:len(eta),0:cont+1]
dspy_mat = dspy_mat[0:len(eta),0:cont+1]


#series inconsistentes
eta_mat_incons = eta_mat_incons[0:len(eta),0:jj+1]
dspx_mat_incons = dspx_mat_incons[0:len(dspx),0:jj+1]
dspy_mat_incons = dspy_mat_incons[0:len(dspy),0:jj+1]

#series consistentes
eta_mat_cons = eta_mat_cons[0:len(eta),0:kk+1]
dspx_mat_cons = dspx_mat_cons[0:len(dspx),0:kk+1]
dspy_mat_cons = dspy_mat_cons[0:len(dspy),0:kk+1]

#quantidade de dados conistentes e inconsistentes
cont_incons = len(lista_inconsistente)
cont_cons = len(lista_consistente)

# ================================================================================== #
##Carrega os dados processados

dados_proc=loadtxt('/home/hppp/Dropbox/Tese/CQ_Python/Boia_MB_RS/Saida_Param_Ondas_Limites.txt',skiprows=1)

#               0     1   2    3      4     5    6    7      8     9      10   11   12   13 
# dados_proc = ano, mes, dia, hora, minuto, Hs, H10, Hmax, Tmed, THmax, HTmax, Hm0, Tp, DirTp

Hs1 = dados_proc[:,5]
H10 = dados_proc[:,6]
Hmax = dados_proc[:,7]
Tmed = dados_proc[:,8]
Tp = dados_proc[:,12]


## Deixa os dados de heave, dspx e dspy em uma coluna

# eta1 = reshape(eta_mat_cons,[size(eta_mat_cons),1])
# dspx1 = reshape(dspx_mat_cons,[size(dspx_mat_cons),1])
# dspy1 = reshape(dspy_mat_cons,[size(dspy_mat_cons),1])


# ================================================================================== #
## Realiza o teste de spike para todas as series

#criar limites de testes	

mult_spike_eta = zeros((1024,kk)) #multiplicador do desvio padrao para o teste de spike - elevacao
lim_spike_eta = zeros((1024,kk))

mult_spike_dspx = zeros((1024,kk)) #multiplicador do desvio padrao para o teste de spike - dspx
lim_spike_dspx = zeros((1024,kk))

mult_spike_dspy = zeros((1024,kk)) #multiplicador do desvio padrao para o teste de spike - dspy
lim_spike_dspy = zeros((1024,kk))

for c in range(kk):

	for i in range(len(eta_mat_cons)):

		#multiplicador do despad para elevacao
		mult_spike_eta[i,c] = ( eta_mat_cons[i,c] - mean(eta_mat_cons[:,c]) ) / std(eta_mat_cons[:,c])

		#limites de spike para elevacao
		lim_spike_eta[i,c] = mult_spike_eta[i,c] * std(eta_mat_cons[:,c])

		#multiplicador do despad para deslocamento x
		mult_spike_dspx[i,c] = ( dspx_mat_cons[i,c] - mean(dspx_mat_cons[:,c]) ) / std(dspx_mat_cons[:,c])

		#limites de spike para deslocamento x
		lim_spike_dspx[i,c] = mult_spike_dspx[i,c] * std(dspx_mat_cons[:,c])

		#multiplicador do despad para elevacao
		mult_spike_dspy[i,c] = ( dspy_mat_cons[i,c] - mean(dspy_mat_cons[:,c]) ) / std(dspy_mat_cons[:,c])

		#limites de spike para elevacao
		lim_spike_dspy[i,c] = mult_spike_dspy[i,c] * std(dspy_mat_cons[:,c])


#deixa o limite de spike em uma coluna (para fazer o histograma)
lim_spike_eta = reshape(lim_spike_eta,[size(lim_spike_eta),1])

#deixa o limite de spike em uma coluna (para fazer o histograma)
lim_spike_dspx = reshape(lim_spike_dspx,[size(lim_spike_dspx),1])

#deixa o limite de spike em uma coluna (para fazer o histograma)
lim_spike_dspy = reshape(lim_spike_dspy,[size(lim_spike_dspy),1])