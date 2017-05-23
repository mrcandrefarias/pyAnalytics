import pandas as pd

filename = '../data/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

def correlation(x, y):
    std_x = (x - x.mean()) / x.std(ddof=0)
    std_y = (y - y.mean()) / y.std(ddof=0)
    return (std_x * std_y).mean()

entries     = subway_df['ENTRIESn_hourly']
cum_entries = subway_df['ENTRIESn']
rain        = subway_df['meanprecipi']
temp        = subway_df['meantempi']

print correlation(entries, rain)
print correlation(entries, temp)
print correlation(rain, temp)

print correlation(entries, cum_entries)
