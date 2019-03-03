import requests
from bs4 import BeautifulSoup

url = 'https://www.nbp.pl/kursy/xml/a223z181116.xml'

response = requests.get(url)
response.encoding = 'utf-8'
content = response.text

result = '<table><tr><th>Nazwa</th><th>Symbol</th><th>Kurs</th></tr>'

soup = BeautifulSoup(content, "html.parser")
nazwy = soup.findAll('nazwa_waluty')
kody = soup.findAll('kod_waluty')
kursy = soup.findAll('kurs_sredni')

for i in range(len(nazwy)):
    #print(nazwy[i].get_text()+" : "+kody[i].get_text()+" : "+kursy[i].get_text())
    result += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (nazwy[i].get_text(), kody[i].get_text(), kursy[i].get_text())
result+= '</table>'
print(result)

with open('kursy.html', 'w') as f:
    f.write(result)


