#funcao para criar datas nos dados da boia MINUANO - RS

#Programa principal: PP_minuano.py

#cria variaveis de ano/mes/dia/hora/min

from datetime import datetime

def data(dados_minuano):

    ano = []
    mes = []
    dia = []
    hora = []
    minuto = []
    datam = []
    
    #cria vetor de tempo(datam)
    for i in range(len(dados_minuano)):
        
        if len(str(dados_minuano[i,0])) == 8:
            
            ano.append(int('20' + str(dados_minuano[i,0])[0:2]))
            
            #vetor de mes
            mes.append(int(str(dados_minuano[i,0])[2:4]))
            
            #vetor de dia
            
            dia.append(int(str(dados_minuano[i,0])[4:6]))
            
        else:
              
            #cria vetor de ano (formato = '2004')
            ano.append(int('200' + str(dados_minuano[i,0])[0]))
     
            mes.append(int(str(dados_minuano[i,0])[1:3]))
          
            dia.append(int(str(dados_minuano[i,0])[3:5]))
    
    	#hora
        if len(str(dados_minuano[i,1])) == 4: #ex: '50.0'
    
    	    hora.append(0)
    
        elif len(str(dados_minuano[i,1])) == 5: #ex: '150.0'
    
    	    hora.append(int(str(dados_minuano[i,1])[0]))
    
        else:
    
        	    hora.append(int(str(dados_minuano[i,1])[0:2]))
    
    
        #minuto (os minutos estao como 50, vamos deixar igual a zero para ficar igual as ondas)
        minuto.append(0)
    
        datam.append(datetime(ano[i],mes[i],dia[i],hora[i],minuto[i]))
        
    return datam,ano,mes,dia,hora,minuto