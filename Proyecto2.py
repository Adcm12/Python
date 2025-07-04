#Extraccion de todos los partidos jugados desde 1930 hasta 2022
from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore
import pandas as pd # type: ignore

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
        1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]

def get_matches(year):
    url = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_='footballbox')

    home = []
    away = []
    scores = []

    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        scores.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())

    dict_football = {'Home Team': home, '  Score': scores, '  Away Team': away}

    df_football = pd.DataFrame(dict_football)
    df_football['Year'] = year

    return df_football

fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa_world_cup_matches.csv', index=False)


df_fixture = get_matches('2022')
df_fixture.to_csv('fifa_world_cup_2022_matches.csv', index=False)
