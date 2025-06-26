from selenium import webdriver #type: ignore
from selenium.webdriver.chrome.service import Service #type: ignore

path = 'C:/Users/adria/Downloads/chrome-win64/chrome-win64.exe'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get('https://en.wikipedia.org/wiki/1982_FIFA_World_Cup')


