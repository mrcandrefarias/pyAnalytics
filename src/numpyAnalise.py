import numpy as np

#Calcula a media de tempo de estudo para estudantes com assinatura
#maior que seis dias
def media_tempo_estudo(horas, assinatura):
    return horas[ assinatura > 6].mean();


tempo_estudo = np.array([
       12.89697233,    0.        ,   64.55043217,    0.        ,
       24.2315615 ,   39.991625  ,    0.        ,    0.        ,
      147.20683783,    0.        ,    0.        ,    0.        ,
       45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
        0.        ,   54.9204785 ,   26.78142417,    0.
])

dias_assinatura = np.array([
      4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
     38,  98,   2, 249,   2, 127,  35
])

print( media_tempo_estudo(tempo_estudo, dias_assinatura) )
