import pandas as pd

df_data_historical = pd.read_csv('fifa_world_cup_matches.csv')
df_fixture = pd.read_csv('fifa_world_cup_2022_matches_fixture.csv')
df_data_faltante = pd.read_csv('fifa_world_cup_2022_matches_missing_data.csv')

print(df_data_historical)
print(df_fixture)
print(df_data_faltante)

