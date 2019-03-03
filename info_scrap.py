import requests
from bs4 import BeautifulSoup

cities = ['Krakow', 'Gdansk', 'Warszawa', 'Lublin', 'Wrocław', 'Poznań', 'Szczecin']

url = 'https://infoshareacademy.com/?s&city='

result = '<table>'
def city_scraper(city):
    table_part ='<tr><th>%s</th></tr>' % (city)
    response = requests.get(url+city)
    plain_text = response.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    paragraphs = soup.findAll('p', {"class": 'course-title'})
    dates = soup.findAll('p', {'class': 'course-info__paragraph course-info__paragraph--date'})
    table_part += '<tr><th>Kurs</th><th>Data</th></tr>'

    for i in range(len(paragraphs)):
        title = paragraphs[i].findAll('span')
        for span in title:
            table_part += '<tr><td>%s</td><td>%s</td></tr>' % (span.contents[0], dates[i].contents[0])
    return(table_part)



for city in cities:
    result += city_scraper(city)

result+='</table>'

with open('infoshare.html', 'w') as f:
    f.write(result)