### PROGRAMA PRINCIPAL PARA PROCESSAMENTO DE DADOS DA BOIA AXYS ###
#
# Desenvolvido por: Henrique P. P. Pereira - heniqueppp@oceanica.ufrj.br
#
# Data da ultima modificacao: 06/09/13
#
# Processamento dos dados de onda da boia Axys do PNBOIA de Recife, 
# no periodo de 2012 a 2013
#
# ================================================================================== #
# Cria uma variavel 'lista' com os arquivos HNE que estao dentro do 'pathname', 
# le e processa cada arquivo HNE listado. Passa por uma consitencia, onde sao 
# listados os arquivos incosistentes e consistentes atribuindo um flag. Processa
# os arquivos consistentes. Chama o modulo 'proc_onda' para processamento dos
# dados no dominio do tempo e frequencia. Cria uma variavel 'mat_onda' contendo
# os parametros calculados. Cria uma tabela 'saida.txt' com os parametros. Cria
# graficos dos parametros.
#
# ================================================================================== #
#
# Subrotinas chamadas: carrega_axys.lista_hne
#					   carrega_axys.dados_hne
#					   consistencia_axys.consiste_bruto
#					   consistencia_axys.consiste_processado
#					   proc_onda.onda_tempo
#					   proc_onda.onda_freq
#					   graficos_axys.graf
#
# ================================================================================== #

# ================================================================================== #
##Importa bibliocas utilizadas

from numpy import *		#modulo para trabalhar com matrizes
from pylab import * 	#importa funcao find
import carrega_axys 	#modulo de listar e atribuir valores dos dados
import proc_onda 		#modulo para processamento dos dados no tempo e frequencia
import consistencia_axys #modulo para realizar a consistencia de dados brutos e processados
import graficos_axys 	#modulo de grafico

# ================================================================================== #
##Dados de entrada

#caminho onde estao os arquivos .HNE
#pathname = '/home/hppp/Dropbox/Tese/PNBOIA_Processamento/HNE/Recife_HNE/'
pathname = 'C:/Users/hppp/Dropbox/Tese/CQ_Python/Processamento/Dados_PNBOIA/Ondas/Recife_HNE/'

#cria arquivo texto com os parameros calculados
arq1 = open('Saida_Param_Axys_Recife.txt','w')

#cria arquivo texto com flags
arq2 = open('Saida_Flags_Axys_Recife.txt','w')

#cabecalho do arquivo (arq1) criado
arq1.write('Ano Mes Dia Hora Min Hs H10 Hmax Tmed THmax HTmax Hm0 Tp DirTp' '\n')

#cria cabecalho do arquivo (arq2) criado
arq2.write('Ano Mes Dia Hora Min Flag' '\n')

#escolhe a data inicial e final para ser processada (opcional, mudar no 'for')
z0 = '201207101500'+'.HNE'
z1 = '201207101600'+'.HNE'

#profundidade da aquisicao
h = 500

#comprimento da serie temporal a ser processada (em potencia de 2)
numproc = 1024

#graus de liberdade
gl = 32

#aplicacao da janela de hanning (han = 1 : hanning / han=0 : retangular)
han = 0

# ================================================================================== #
##Lista arquivos .HNE que estao dentro do diretorio 'pathname'

#cria lista com o nome dos arquivos
lista = carrega_axys.lista_hne(pathname)

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

fasennx = []  #fase entre eta e dspx (aproximadamente 90 graus)
fasenny = []  #fase entre eta e dspy (aproximadamente 90 graus)
fasenxny = [] #fase entre dspx e dspy (aproximadamente 0 grau)

coernnx = []  #coerencia entre eta e dspx
coernny = [] #coerencia entre eta e dspy
coernxny = [] #coerencia entre dspx e dspy

ind_fw = [] #posicao do registro dentro de lista_consistentes 
rel_fw = [] #
flag_fw = []
reg_fw = []

Hmax_fw = [] #parametros para entender as freawaves
Hs_fw = []
Hm0_fw = []
THmax_fw = []

rel_Hmax_Hs = [] #relacao de Hmax/Hs para todas as ondas 'consistentes'

# ================================================================================== #
## Le os dados de um arquivo e processa

#acha o indice na variavel lista dos arquivos escolhidos para serem processados 
p0 = find(array(lista) == z0)
p1 = find(array(lista) == z1) + 1 #coloca +1 para pegar registro p1

#colunas do eta_mat (cada coluna eh uma hora)
jj = -1   #contador de arquivos inconsistentes
kk = -1   #contador de arquivos consistentes
cont = -1 #contador de arquivos (dimensao da matriz com series temporais)

for i in range(len(lista)):  #le todos os arquivos da lista
#for i in range(p0,p1):		  #le os arquivos escolhidos

	#contador de arquivos analisados
	cont = cont + 1
	
	#atribui o nome do arquivo a variavel 'arq'
	arq = lista[i]

	#cria variavel string do nome dos arquivos
	lista_arq.append(arq)

	#atribui as variaveis em 'dados' e a data em 'data'
	dados, data = carrega_axys.dados_hne(pathname,arq)

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

	#coloca cada serie temporal em uma coluna (tanto os consistentes como os inconsistentes)
	eta_mat[0:len(eta),cont] = eta
	dspx_mat[0:len(dspx),cont] = dspx
	dspy_mat[0:len(dspy),cont] = dspy

	# ================================================================================== #
	## Faz a consistencia dos dados brutos

	#importa modulo de consistencia e funcao da conistencia de dados brutos
	flag = consistencia_axys.consiste_bruto(t,eta,dspy,dspx,arq)

	# flag = '0' - passou na consistencia de dados brutos

	#Dados que receberem flags (flag diferente de '0') nao serao processados)
	#O dado ate poderia ser processado. mas provavelmente dara erro antes de 
	#processar todos os dados. Entao para o caso de consistencia em terra,
	#vale qualificar um flag nesses dados e depois processar os mesmos.

	#Se o flag for diferente de zero (quer dizer que recebeu flag)
	if flag <> '0': 

		#cria lista com o nome dos arquivos inconsisentes
		lista_inconsistente.append(int(arq[0:12]))

		#preenche lista de flags de todos os arquivos
		lista_flag.append([ano, mes, dia, hora, minuto, flag])

		#cria matriz com series temporais reprovadas na consistencia
		jj = jj + 1 #contador de colunas (cada coluna eh uma hora)
		
		#coloca serie temporal em cada coluna (inconsistentes)
		eta_mat_incons[0:len(eta),jj] = eta
		dspx_mat_incons[0:len(dspx),jj] = dspx
		dspy_mat_incons[0:len(dspy),jj] = dspy
		
		#cria saida em txt de flags
		arq2.write('%i %.2i %.2i %.2i %.2i %s \n' % (ano, mes, dia, hora, minuto, flag))
	
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

		# ================================================================================== #	
		## Processamento no dominio do tempo
		
		#Dados de entrada: t - vetor de tempo
		#				   eta - elevacao
		#				   h - profundidade
		#Dados de saida: sai_ondatempo - vetor com parametros de onda calculados no dominio do tempo

		sai_ondatempo = proc_onda.onda_tempo(t,eta,h)

		#definicao dos parametros de onda no dominio do temporaisP
		[Hs,H10,Hmin,Hmax,Hmed,Tmin,Tmax,Tmed,THmax,HTmax,Lmin,Lmax,Lmed,Cmed] = sai_ondatempo

		# ================================================================================== #	
		## Processamento no dominio da frequencia

		#Dados de entrada: t - vetor de tempo
		#				   eta - elevacao
		#				   dspy - deslocamento norte
		#				   dspx - deslocamento leste
		#				   gl - graus de liberdade
		#				   han - aplicacao da janela de hanning (1 = hanning ; 0 = retangular)
		#				   h - profundidade
		#Dados de saida: sai_ondafreq - vetor com parametros de onda calculados no dominio da freq.

		sai_ondafreq, k, aannx, aanny, aanxny, a1, b1, diraz = proc_onda.onda_freq(t,eta,dspy,dspx,gl,han,h)

		#definicao dos parametros de onda no dominio da frequencia
		[Hm0, Tp, DirTp] = sai_ondafreq

		# ================================================================================== #	
		## Cria variavel com os parametros calculados

		#				  0    1    2     3     4     5      6     7    8    9
		mat_onda.append([Hs, H10, Hmax, Tmed, Tmax, THmax, HTmax, Hm0, Tp, DirTp])

		# ================================================================================== #
		## Calcula a relacao de Hmax/Hs (para freakwaves)

		rel_Hmax_Hs.append(Hmax / Hs)

		# ================================================================================== #	
		## Consistencia dos parametros de ondas calculados (freakwave - tomar cuidado pois soh estamos analisando os dados 'consistentes'

		ind_fw_aux, rel_fw_aux, flag_fw_aux, reg_fw_aux, aann, aanxnx, aanyny, k1 = consistencia_axys.consiste_processado(
		t, eta, dspy, dspx, aannx, aanny, aanxny, gl, han, Hs, Hmax, arq, kk)

		# figure()
		# plot(aannx[:,0],k1)
		# savefig('numeronda'+str(cont))

		if flag_fw_aux <> '0':

			rel_fw.append(rel_fw_aux)
			flag_fw.append(flag_fw_aux)
			ind_fw.append(ind_fw_aux)
			reg_fw.append(reg_fw_aux)

			#salva informacoes importantes das freakwaves
			Hmax_fw.append(Hmax) #altura da freakwave (altura maxima da serie)
			Hs_fw.append(Hs) #altura significativa da serie
			Hm0_fw.append(Hm0) #altua significativa (espectro)
			THmax_fw.append(THmax) #periodo associado a altura maxima

			#para entrar o flag de freakwave dentro da lista_flag
			flag = flag_fw_aux
			
			#coloca na lista de flags os arquivos que possuem freakwaves
			lista_flag.append([ano, mes, dia, hora, minuto, flag])

		else:

			lista_flag.append([ano, mes, dia, hora, minuto, flag])
			
		# ================================================================================== #	
		## Calcula as fases das series de elevacao e deslocamentos
		aux_fasennx = list(aannx[(find(aannx[:,3] == max(aannx[:,3])),6)])
		aux_fasenny = list(aanny[(find(aanny[:,3] == max(aanny[:,3])),6)])
		aux_fasenxny = list(aanxny[(find(aanxny[:,3] == max(aanxny[:,3])),6)])

		## Cria um vetor com as fases
		fasennx.append(aux_fasennx)
		fasenny.append(aux_fasenny)
		fasenxny.append(aux_fasenxny)

		## Calcula as coerencias das series de elevacao e deslocamentos
		aux_coernnx = list(aannx[(find(aannx[:,3] == max(aannx[:,3])),7)])
		aux_coernny = list(aanny[(find(aanny[:,3] == max(aanny[:,3])),7)])
		aux_coernxny = list(aanxny[(find(aanxny[:,3] == max(aanxny[:,3])),7)])

		## Cria um vetor com as coerencias
		coernnx.append(aux_coernnx)
		coernny.append(aux_coernny)
		coernxny.append(aux_coernxny)

		# ================================================================================== #	
		## Monta arquivo texto de saida

		#parametros de onda processados
		arq1.write('%i %.2i %.2i %.2i %.2i %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f \n'
		% (ano, mes, dia, hora, minuto, Hs, H10, Hmax, Tmed, THmax, HTmax, Hm0, Tp, DirTp))

		#flags
		arq2.write('%i %.2i %.2i %.2i %.2i %s \n' 
		% (ano, mes, dia, hora, minuto, flag))

# ================================================================================== #
## Series temporais de eta, dspy e dspx

#### Observacao: ####
#tomar cuidado, pois alguns vetores que tem o comprimento menor que 1024, vai ser
#preenchido com nan, isso mascara o comprimento real do vetor quando se usa o 'len'
#para ver o comprimento real do vetor, melhor verificar plotando a figura, ou descobrir um 
#jeito de calcular o comprimento exluindo os nan

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

#quantidade de freakwaves
#cont_freak = len(ind_freak)

# ================================================================================== #	
## Transforma em matriz os parametros e os flags (linha=registros , coluna=parametros)

#Parametros 
mat_onda = array(mat_onda)

#Flags
lista_flag = array(lista_flag)

#tabela de elevacao das freakwaves
eta_mat_fw = eta_mat_cons[:,ind_fw]

# ================================================================================== #	
## Salva o arquivo de saida
arq1.close()
arq2.close()

# ================================================================================== #	
## Cria graficos
graficos_axys.graf(mat_onda,eta_mat_cons,dspx_mat_cons,dspy_mat_cons,reg_fw,Hmax_fw,Hs_fw,THmax_fw,rel_fw,ind_fw)

# figure()

# hist(mult_spike)

show()