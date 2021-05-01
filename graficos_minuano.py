#graficos das series temporais da boia MINUANO - Rio Grande do Sul

from pylab import *

def graficos(datam,at,at_c,rh,rh_c,ws1,ws1_c,ws2,ws2_c,wg1,wg1_c,wg2,wg2_c,wd1,wd1_c,wd2,wd2_c,wt,wt_c,bp,bp_c,sigw,sigw_c,sigp,sigp_c,maxw,maxw_c,sr,sr_c):

    #graficos dos parametros

    #temperatura do ar    
    figure()
    plot_date(datam,at,'bo')
    plot_date(datam,at_c,'ro')
    legend(('bruto','consistente'))
    ylabel('Graus Celsius')    
    title('Temperatura do Ar')
    
    figure()
    plot_date(datam,rh)
    plot_date(datam,rh_c,'ro')
    legend(('bruto','consistente'))
    ylabel('%')    
    title('Umidade Relativa')
    
    figure()
    plot_date(datam,ws1)
    plot_date(datam,ws1_c,'ro')
    legend(('bruto','consistente'))
    ylabel('m/s')    
    title('Velocidade do Vento - 1')

    figure()
    plot_date(datam,ws2)
    plot_date(datam,ws2_c,'ro')
    legend(('bruto','consistente'))
    ylabel('m/s')
    title('Velocidade do Vento - 2')

    figure()
    plot_date(datam,wg1)
    plot_date(datam,wg1_c,'ro')
    legend(('bruto','consistente'))
    ylabel('m/s')
    title('Velocidade de Rajada do Vento - 1')

    figure()
    plot_date(datam,wg2)
    plot_date(datam,wg2_c,'ro')
    legend(('bruto','consistente'))
    ylabel('m/s')
    title('Velocidade de Rajada do Vento - 2')
    
    figure()
    plot_date(datam,wd1)
    plot_date(datam,wd1_c,'ro')
    legend(('bruto','consistente'))
    ylabel('m/s')
    title('Direcao do Vento - 1')
    
    figure()
    plot_date(datam,wd2)
    plot_date(datam,wd2_c,'ro')
    legend(('bruto','consistente'))
    ylabel('Graus')
    title('Direcao do Vento - 2')

    figure()
    plot_date(datam,wt)
    plot_date(datam,wt_c,'ro')
    legend(('bruto','consistente'))
    ylabel('Graus Celsius')
    title('Temperatura da Agua')

    figure()
    plot_date(datam,bp)
    plot_date(datam,bp_c,'ro')
    legend(('bruto','consistente'))
    ylabel('hPa')
    title('Pressao Atmosferica')
    
    figure()
    plot_date(datam,sigw)
    plot_date(datam,sigw_c,'ro')
    legend(('bruto','consistente'))
    ylabel('metros')
    title('Altura Significativa de Onda')

    figure()
    plot_date(datam,maxw)
    plot_date(datam,maxw_c,'ro')
    legend(('bruto','consistente'))
    ylabel('metros')
    title('Altura Maxima de Onda')

    figure()
    plot_date(datam,sr)
    plot_date(datam,sr_c,'ro')
    legend(('bruto','consistente'))
    ylabel('W/m2')
    title('Radiacao Solar')
        
#    figure()
#    subplot(3,1,1)
#    plot_date(datam,bp), title('Pressao Atmosferica'), ylabel('hPa')
#    subplot(3,1,2)
#    plot_date(datam,ws1), title('Velocidade do Vento'), ylabel('m/s')
#    subplot(3,1,3)
#    plot_date(datam,sigw), title('Altura Significativa'), ylabel('metros')
    
    

    
 