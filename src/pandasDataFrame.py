import pandas as pd

passageiros = pd.DataFrame(
    data=[[   0,    0,    2,    5,    0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [  95,  229,  255,  496,  201],
          [   2,    0,    1,   27,    0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)


if False:
    df_1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print df_1

    df_2 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=['A', 'B', 'C'])
    print df_2


if False:
    print passageiros.iloc[0] #linha zero. Busca por posicao
    print passageiros.loc['05-05-11'] # buca por indice
    print passageiros['R003'] # busca por coluna
    print passageiros.iloc[1, 3] #linha 1 coluna tres

# Accessing multiple rows
if False:
    print passageiros.iloc[1:4]

# Accessing multiple columns
if False:
    print passageiros[['R003', 'R005']]

# Pandas axis
if False:
    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print df.sum()
    print df.sum(axis=1) #axis=1 linhas
    print df.values.sum()

def mean_riders_for_max_station(passageiros):
    maxStation   = passageiros.iloc[0].argmax() #pega posicao do valor maximo linha um
    mean_for_max = passageiros[maxStation].mean()
    overall_mean = passageiros.values.mean()
    return {'overall_mean':overall_mean, 'mean_for_max_firstDay': mean_for_max}

#print mean_riders_for_max_station(passageiros)

sb = pd.read_csv('../data/nyc_subway_weather.csv')

print(sb.head())

print(sb.describe())
