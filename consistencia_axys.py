##Rotina de consistencia para a boia axys

from numpy import *
from pylab import *
from espectro import *

def consiste_bruto(t,eta,dspy,dspx,arq):

	##arq = nome do arquivo (para verificar validade da mensagem recebida)

	#flag de dados consistentes
	flag = ''

	#1-verifica a validade na mensagem recebida
	
	#se os dados foram programados para serem enviados em hora cheia (min=00),
	#observa se os mesmos estao diferentes de 00
		
	if arq[10:12] <> '00':

		flag = flag + '1'

	#2- verifica comprimento do vetor
	if len(eta) < 1024:

		flag = flag + '3'

	#3- verifica se todos os valores estao zerados
	if (eta==0).all():

		flag = flag + '2'

	#4- verifica se todos os valores de eta sao muito proximos de zero
	if ( (eta < 0.1).all() and (eta > - 0.1).all() ):

		flag = flag + '4'

	#5- verifica valores consecutivos nulos (por enquanto, 5 valores iguais (ncn))
	#fazer com o eta, dspx e dspy

	ncn = 5
	for i in range(len(eta)-ncn):

		if (eta[i:i+ncn] == 0).all():

			flag = flag + '5'

			break

	#6- verifica valores consecutivos iguais (nci)

	nci = 5
	for i in range(len(eta)-(nci+1)):

		if (eta[i:i+nci] == eta[i+1:i+1+nci]).all():

			flag = flag + '6'

			break

	#7- teste de range (de acordo com o limite dos equipamentos)

	#limites de range
	lrmax = 20
	lrmin = -20

	if ( (eta > lrmax).any() or (eta < lrmin).any() ):

		flag = flag + '7'

		#plota series reprovadas
		#figure(), plot(eta), title(arq), show()

	#8- teste de spike (limites regionais, que podem selecionar valores importantes)

	lsmax = 5
	lsmin = -5
	
	if ( (eta > lsmax).any() or (eta < lsmin).any() ):

		flag = flag + '8'

		#plota series reprovadas
		#figure(), plot(eta), title(arq), show()








	#se nao reprovou em nenhum teste
	if flag == '':

		flag = '0'

	#teste de valores consecutivos iguais (verificar quantos valores)
	# elif flag == 0:

	# 	for i in range(len(eta)-3):

	# 		if eta[i:i+3] == eta[i]:

	# 			flag = 1


	return flag


def consiste_processado(t, eta, dspy, dspx, aannx, aanny, aanxny, gl, han, Hs, Hmax, arq, kk):

	# ================================================================================== #

	#verifica se ha freak wave no registro
	#calcula a relacao entre Hmax/Hs maior que 2.1

	#Hs = mat_onda[:,0]
	#Hmax = mat_onda[:,2]

	#flag para freakwave
	flag_fw_aux = ''

	#calcula relacao para freak wave
	rel_fw_aux = Hmax / Hs

	#se a relacao for maior que 2.1, 
	if rel_fw_aux > 2.1:

		#acha o indice do registro da freak wave dentro na lista de lista_consistentes

		flag_fw_aux = 'freakwave'
		ind_fw_aux = kk
		reg_fw_aux = arq

		#acha os indices das freakwaves dentro da lista de dados consistentes (mudar para dados processados)
		#ind1_fw = list(find(array(lista_consistente) == int(arq[0:12])))

		#acha o nome dos registros que consideramos ter freakwaves

	if flag_fw_aux == '':

		flag_fw_aux = '0'
		ind_fw_aux = []	
		reg_fw_aux = []

		# return rel_fw, flag_fw, reg_fw


	#acha as posicoes dos registros que contem freak waves
	#ind_freak = find(rel_freak > 2.1)

	#contador de registros com freak waves
	#cont_freak = len(ind_freak)

	#cria lista com os registros que contem freak waves
	#reg_freak = [lista_consistente[i] for i in ind_freak]

	# ================================================================================== #
	## Check-Ratio

	#intervalo de tempo
	dt = t[1]-t[0]

	#calculo dos espectros cruzados
	aann = espec2(eta,eta,dt,gl,han)
	aanxnx = espec2(dspx,dspx,dt,gl,han)
	aanyny = espec2(dspy,dspy,dt,gl,han)
	
	#check ratio
	#calculo do 'k' pelo espec cruzado
	k1 = sqrt( (aannx[:,2] + aanny[:,2]) / aannx[:,1] )




	return ind_fw_aux, rel_fw_aux, flag_fw_aux, reg_fw_aux, aann, aanxnx, aanyny, k1