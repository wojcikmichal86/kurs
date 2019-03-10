from find_all_links import get_page
from parsel import Selector

if __name__ == '__main__':
    filename = 'otomoto.html'
    url = 'https://www.otomoto.pl/oferta/mercedes-benz-klasa-g-ID6Byg3J.html'
    content = get_page(filename, url)
    selector = Selector(text=content)
    wszystko =  selector.xpath('//span[@class = "offer-main-params__item"]/text()').getall()
    tytul = selector.xpath('//h1[@class = "offer-title big-text"]/text()').getall()[1].rstrip().strip()
    rocznik = wszystko[0].rstrip().strip()
    przebieg = wszystko[1].rstrip().strip()
    typ_silnika = wszystko[2].rstrip().strip()
    klasa_auta = wszystko[3].rstrip().strip()
    cena = selector.xpath('//span[@class = "offer-price__number"]/text()').getall()[0].rstrip().strip()
    print(tytul)
    print(rocznik)
    print(przebieg)
    print(typ_silnika)
    print(cena)
    print(klasa_auta)
