from homework_create_engine import Session
import json
from pprint import pprint

if __name__ == '__main__':
    from homework_models import Portale, Kampania, Oferty
    session = Session()
    allegro = Portale(nazwa_portalu='allegro')
    session.add(allegro)
    session.commit()
    kamp_allegro = Kampania(data='2018.11.31', id_portalu=allegro.id)
    session.add(kamp_allegro)
    session.commit()
    with open('oferty.json') as file:
        data = json.load(file)

    for offer in data.keys():
        values = data[offer]
        oferta = Oferty(
        id_kampanii = kamp_allegro.id,
        id_oferty = str(offer),
        id_sprzedajacego = values['sprzedający'],
        lokalizacja = values['lokalizacja'],
        tytul = 'Brak informacji',
        cena = int(values['cena'][:-3]),
        marka = values['marka'],
        model = values['model'],
        rok_produkcji = int(values['Rok produkcji']),
        przebieg = int(values['Przebieg'][:-3]),
        pojemnosc = int(values['Pojemność silnika'][:-3]),
        moc = int(values['Moc'][:-3]),
        rodzaj_paliwa = values['Rodzaj paliwa'],
        kolor = values['Kolor'],
        uszkodzony = values['Uszkodzony'],
        kraj = values['Kraj pochodzenia'],
        naped = values['Napęd'],
        liczba_miejsc = values['Liczba miejsc'])
        session.add(oferta)
        session.commit()


