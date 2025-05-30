import pandas as pd # type: ignore
import numpy as np # type: ignore

# Create a DataFrame with random data
data = np.array([[1,4], [2,5], [3,6], [4,7], [5,8]])
df = pd.DataFrame(data, index = 'row.1 row.2 row.3 row.4 row.5'.split(), columns = 'col.1 col.2'.split())

print("\nOriginal DataFrame:\n")
print(df)

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California']
population = [4903185, 731545, 7278717, 3017804, 39538223]

dict_data = {'state': states, 'population': population}
df2 = pd.DataFrame(dict_data)
print("\nDataFrame from dictionary:\n")
print(df2)

df_exams = pd.read_csv('BD_anuario.csv')
print("\nDataFrame from CSV file primeras 5 filas:\n")
print(df_exams.head())
print("\nDataFrame from CSV file ultimas 5 filas:\n")
print(df_exams.tail())
print("\nDataFrame from CSV file solo algunas lineas:\n")
print(df_exams.head(12))
      
print("atributo shape")
print(df_exams.shape)
