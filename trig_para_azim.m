function [diraz]=trig_para_azim(dirt)
%Programa que muda direção que estão no padrão
%do arco trigonométrico (90º=norte) para direção em azimute (0º=norte)

%Dados de entrada: direção em trigonométrico
%Dados de saída: Direção corrigida para azimute

for i=1:length(dirt)
    if dirt(i,1)>=0 & dirt(i,1)<=90
        diraz(i,1)=90-dirt(i);
    elseif dirt(i,1)>90 & dirt(i,1)<=180
        diraz(i,1)=90+(360-dirt(i,1));
    elseif dirt(i,1)>180 & dirt(i,1)<=270
        diraz(i,1)=180+(270-dirt(i,1));
    elseif dirt(i,1)>270 & dirgrau1(i,1)<=360 | dirt(i,1)<0 & dirt(i,1)>=-90
        diraz(i,1)=(270+(180-dirt(i,1)))-360;
    end
end
