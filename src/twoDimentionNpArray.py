import numpy as np
'''
Em um np.array todos os elementos devem ser do mesmo tipo.
Caso nao sejam, numpy os tratara como strings
'''

# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])

if False:
    print ridership[1, 3] # coluna 3 da linha 1
    print ridership[1:3, 4:3]#4:3 colunas da linha 1.
    print ridership[1, :] #todas as colunas da linha 1


if False:
    print ridership[0, :] + ridership[1, :]
    print ridership[:, 0] + ridership[:, 1] # coluna 0 + coluna 1. Todas as linhas, coluna zero zero ([:, 0])

if False:
    a = np.array([[1, 2], [4, 5], [7, 8]]) #3 linhas e 2 colunas
    b = np.array([[1, 1], [2, 2], [3, 3]]) #3 linhas e 2 colunas
    print a + b

def mean_riders_for_max_station(ridership):
    #maior valor da linha zero
    #ridership[0, :].max();
    maxStation   = ridership[0, :].argmax() #pega posicao do valor maximo linha um
    mean_for_max = ridership[:, maxStation].mean()
    overall_mean = ridership.mean()
    return {'overall_mean':overall_mean, 'mean_for_max_firstDay': mean_for_max}

#print(mean_riders_for_max_station(ridership))

def min_and_max_riders_per_day(ridership):
    # mean ridership per day for each station
    mean_station_ridership = ridership.mean(axis=0) #axis=0 todas as colunas
    max_daily_ridership    = mean_station_ridership.max()
    min_daily_ridership    = mean_station_ridership.min()

    return (max_daily_ridership, min_daily_ridership)

#print( min_and_max_riders_per_day(ridership) )
