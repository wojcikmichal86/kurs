import os
from parsel import Selector


def load_offer(_offer):
    file_name = os.path.join('data', _offer)
    with open(file_name, encoding='utf-8') as _file_in:
        _data = _file_in.read()

    return _data


def get_details(_data):
    selector = Selector(text=_data)

    # selector css object wskazujący na tytuł strony
    # zapisy alternatywne
    #print(selector.css('title::text'))
    #print(selector.css('head > title::text'))

    # by wydobyć tekst z HTML trzeba skorzystać z konstrukcji poniżej
    # zapisy alternatywne
    #print(selector.css('title::text').get())
    #print(selector.css('head > title::text').get())

    # TODO: dodaj kolejne etykietki
    # Uwaga! - Te selektory zostały wygenerowane przez Chrome. FF może zapisać inaczej
    if 'Faktura VAT' in str(selector.css('span.offer-price__details:nth-child(2)::text').get()):
        print('Faktura: Tak')
    else:
        print('Faktura: Nie')
    """
    if 'Cena Brutto' in str(selector.css('span.offer-price__details:nth-child(2)::text').get()):
        print('Cena Brutto: Tak')
    else:
        print('Cena Brutto: Nie')
    """
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(2) > span::text').get(), ' ', end="")
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(2) > div > a::attr(title)').get())
    print('Marka: '+selector.css('#parameters > ul:nth-child(1) > li:nth-child(3) > div > a::attr(title)').get())
    print('Model: '+selector.css('#parameters > ul:nth-child(1) > li:nth-child(4) > div > a::attr(title)').get())
    print('Wersja: '+selector.css('#parameters > ul:nth-child(1) > li:nth-child(5) > div > a::attr(title)').get())
    print('Rok produkcji: '+selector.css('#parameters > ul:nth-child(1) > li:nth-child(6) > div::text').get().strip())
    print('Przebieg: '+selector.css('#parameters > ul:nth-child(1) > li:nth-child(7) > div::text').get().strip())
    print('Pojemność: '+selector.css('#parameters > ul:nth-child(1) > li:nth-child(8) > div::text').get().strip())
    print('Rodzaj paliwa: '+selector.css('#parameters > ul:nth-child(1) > li:nth-child(9) > div > a::attr(title)').get().strip())
    print('Moc: '+selector.css('#parameters > ul:nth-child(1) > li:nth-child(10) > div::text').get().strip())
    print('Skrzynia biegów: '+selector.css('#parameters > ul:nth-child(1) > li:nth-child(11) > div > a::attr(title)').get().strip())
    print('Napęd: '+str(selector.css('#parameters > ul:nth-child(1) > li:nth-child(12) > div > a::attr(title)').get()))
    print('Typ: '+str(selector.css('#parameters > ul:nth-child(1) > li:nth-child(13) > div > a::attr(title)').get()))
    print('Liczba drzwi: '+str(selector.css('#parameters > ul:nth-child(1) > li:nth-child(14) > div::text').get()).strip())
    print('Liczba miejsc: '+selector.css('#parameters > ul:nth-child(2) > li:nth-child(1) > div::text').get().strip())
    print('Kolor: '+selector.css('#parameters > ul:nth-child(2) > li:nth-child(2) > div > a::text').get().strip())
    # TODO: dodaj wyszukiwanie waluty
    print("Waluta: " + str(selector.css('.offer-price__currency::text').get()).strip())
    # TODO: dodaj wyszukiwanie lokalizacji
    print("Lokalizacja: " + str(selector.css('.seller-box__seller-address__label::text').get()).strip())

offers = (
    'ford-focus-salon-polska-klima-sprawy-zadbany-polecam-ID6BxpMS.html',
    'ford-focus-1-6-tdci-salon-polska-serwis-aso-klima-ID6BwGlg.html'
)
for offer in offers:
    data = load_offer(offer)
    get_details(data)
    print('-' * 40)
