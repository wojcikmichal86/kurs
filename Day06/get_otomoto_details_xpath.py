import os
from parsel import Selector


def load_offer(_offer):
    file_name = os.path.join('data', _offer)
    with open(file_name, encoding='utf-8') as _file_in:
        _data = _file_in.read()
    #print(_data)
    return _data


def get_details(_data):
    selector = Selector(text=_data)

    if 'Faktura VAT' in str(selector.xpath('//span[@class="offer-price__details"]/text()').get()):
        print('Faktura: Tak')
    else:
        print('Faktura: Nie')

    """
    if 'Cena Brutto' in str(selector.xpath('//span[@class="offer-price__details"]/text()').get()):
        print('Cena Brutto: Tak')
    else:
        print('Cena Brutto: Nie')
    """
    # selector xpath object wskazujący na tytuł strony
    #print(selector.xpath('//title/text()'))

    # by wydobyć tekst z HTML trzeba skorzystać z konstrukcji poniżej
    print(selector.xpath('//title/text()').get())  # pojedynczy, pierwszy rezultat

    # TODO: dodaj kolejne etykietki
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[2]/span/text()').get(), ' ', end="")
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[2]/div/a/@title').get())
    print('Marka: '+selector.xpath('//*[@id="parameters"]/ul[1]/li[3]/div/a/text()').get().strip())
    print('Model: '+selector.xpath('//*[@id="parameters"]/ul[1]/li[4]/div/a/text()').get().strip())
    print('Wersja: '+selector.xpath('//*[@id="parameters"]/ul[1]/li[5]/div/a/text()').get().strip())
    print('Rok produkcji: '+selector.xpath('//*[@id="parameters"]/ul[1]/li[6]/div/text()').get().strip())
    print('Przebieg: '+selector.xpath('//*[@id="parameters"]/ul[1]/li[7]/div/text()').get().strip())
    print('Pojemnośc: '+selector.xpath('//*[@id="parameters"]/ul[1]/li[8]/div/text()').get().strip())
    print('Rodzaj paliwa: '+selector.xpath('//*[@id="parameters"]/ul[1]/li[9]/div/a/@title').get())
    print('Moc: '+selector.xpath('//*[@id="parameters"]/ul[1]/li[10]/div/text()').get().strip())
    print('Skrzynia biegow: '+selector.xpath('//*[@id="parameters"]/ul[1]/li[11]/div/a/@title').get())
    print('Napęd: '+str(selector.xpath('//*[@id="parameters"]/ul[1]/li[12]/div/a/@title').get()))
    print('Typ: '+str(selector.xpath('//*[@id="parameters"]/ul[1]/li[13]/div/a/@title').get()))
    print('Liczba drzwi: '+str(selector.xpath('//*[@id="parameters"]/ul[1]/li[14]/div/text()').get()).strip())
    print('Liczba miejsc: ' + str(selector.xpath('//*[@id="parameters"]/ul[2]/li[1]/div/text()').get()).strip())
    print('Kolor: ' + str(selector.xpath('//*[@id="parameters"]/ul[2]/li[2]/div/a/text()').get()).strip())


    # TODO: dodaj wyszukiwanie waluty
    print("Waluta: "+str(selector.xpath('//span[@class="offer-price__currency"]/text()').get()))
    # TODO: dodaj wyszukiwanie lokalizacji
    print("Lokalizacja: " + str(selector.xpath('//span[@class="seller-box__seller-address__label"]/text()').get().strip()))


offers = (
    'ford-focus-salon-polska-klima-sprawy-zadbany-polecam-ID6BxpMS.html',
    'ford-focus-1-6-tdci-salon-polska-serwis-aso-klima-ID6BwGlg.html'
)
for offer in offers:
    data = load_offer(offer)
    get_details(data)
    print('-' * 40)
