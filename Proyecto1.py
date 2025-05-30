#Prediccion del ganador de Qatar 2022
import pandas as pd # type: ignore
from string import ascii_uppercase as alfabeto 
import pickle

url = 'https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'

todas_las_tablas = pd.read_html(url)
#indices_tablas = [12, 19, 26, 33, 40, 47, 54, 61]

dict_tablas ={}

for letra, i in zip(alfabeto, range(12, 68, 7)):
    df = todas_las_tablas[i]
    df.rename(columns={df.columns[1]: 'Team'}, inplace=True)
    df.pop('Qualification')
    dict_tablas[f'Grupo {letra}'] = df

with open('datos_mundial.txt', 'wb') as output:
    pickle.dump(dict_tablas, output)
