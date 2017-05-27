import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Group by single column
if False:
    grouped_data = example_df.groupby('even')
    print grouped_data.groups

# Group by multiple columns
if False:
    grouped_data = example_df.groupby(['even', 'above_three'])
    print grouped_data.groups

# Sum of each group
if False:
    grouped_data = example_df.groupby('even')
    print grouped_data.sum()

# Group by speciffic column
if False:
    grouped_data = example_df.groupby('even')
    # You can take one or more columns
    print grouped_data.sum()['value']
    print '\n'
    # OR
    print grouped_data['value'].sum()

filename = '../data/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

#print subway_df.head()
passageiros_dia = subway_df.groupby('day_week').mean()['ENTRIESn_hourly']
#passageiros_dia.plot()
#sns.plt.show() #show in linux terminal

location = subway_df.groupby( ['latitude', 'longitude'], as_index=False ).mean()
plt.scatter(location['latitude'], location['longitude'] )
sns.plt.show()
