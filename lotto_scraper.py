import requests
from bs4 import BeautifulSoup
import string

url = 'https://www.lotto.pl'

response = requests.get(url)
response.encoding = 'utf-8'
content = response.text

with open('lotto.txt', 'w') as f:
    f.write(content)

soup = BeautifulSoup(content, features="html.parser")

box = soup.find('div', {'class': 'resultsOpen'})

games = ['resultsItem lotto', 'resultsItem lottoPlus', 'resultsItem lottoSzansa', 'resultsItem euroJackpot', 'resultsItem EkstraPensja', 'resultsItem EkstraPensjaSzansa', 'resultsItem MiniLotto', 'resultsItem MiniLottoSzansa', 'resultsItem multiMulti', 'resultsItem multiMultiSzansa', 'resultsItem zs']
names = []
times = []
for game in games:
    result = []
    div = soup.find('div', {"class": game})
    name = div.find("a")
    date = div.find('strong')
    text = name.get_text(strip=True)
    clean_text = text.replace("\\t", "")
    clean_text = clean_text.replace("\\n", "")
    print('Nazwa gry: '+clean_text.strip())
    try:
        print('Data: '+date.get_text())
    except:
        pass
    numbers = div.findAll('div', {'class': 'number text-center'})
    for number in numbers:
        result.append(number.find('span').get_text())
    print(result)










    #print(h2.contents)

#print(soup.prettify())

'''
number_position = content[results_position:].find('number text-center ')

number_result = content[results_position:][number_position:]

first_number = number_result.find('span')

print(number_result[first_number+5])

results = []

text_to_find = 'span'

while len(results)<6:
    first_number = number_result.find(text_to_find)
    winning_number = number_result[first_number+5]
    if number_result[first_number+6].isnumeric():
        winning_number += number_result[first_number+6]

    results.append(winning_number)
    number_result = number_result[first_number+10:]


print(results)

text_to_find = '<span>'
text_to_find2 = '</span>'
span_position1 = content.find(text_to_find, first_number)
span_position2 = content.find(text_to_find2, span_position1)

print(content[span_position1+len(text_to_find):span_position2])
'''