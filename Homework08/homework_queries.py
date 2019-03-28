from homework_create_engine import Session
from homework_models import Kampania, Portale, Oferty
from sqlalchemy import func

def query_all(klasa):
    for item in session.query(klasa).all():
        print(item)

def count_all(klasa):
    all_items = session.query(klasa).all()
    print(len(all_items))

def by_model(klasa):
    mk3=[]
    for item in session.query(klasa).filter(klasa.model == 'Mk3 (2010-)'):
        mk3.append(item)
    print('Mk3 (2010-): '+str(len(mk3)))
    e60=[]
    for item in session.query(klasa).filter(klasa.model == 'E60 (2003-2010)'):
        e60.append(item)
    print('E60 (2003-2010): '+str(len(e60)))

def max_price(model):
    max_cena = session.query(func.max(Oferty.cena)).filter(Oferty.model == model)
    print('Model: '+model+' - maksymalna cena: '+str(max_cena[0])[1:-2])

def min_price(model):
    min_cena = session.query(func.min(Oferty.cena)).filter(Oferty.model == model)
    print('Model: '+model+' - minialna cena: '+str(min_cena[0])[1:-2])

def max_przebieg(model):
    max_przeb = session.query(func.max(Oferty.przebieg)).filter(Oferty.model == model)
    print('Model: '+model+' - maksymalny przebieg: '+str(max_przeb[0])[1:-2])

def min_przebieg(model):
    min_przeb= session.query(func.min(Oferty.przebieg)).filter(Oferty.model == model)
    print('Model: '+model+' - minialny przebieg: '+str(min_przeb[0])[1:-2])

if __name__ == '__main__':
    session = Session()
    wybor = ''
    while wybor != 'q':
        wybor = input('\nWybierz opcję:\n'
                      '1 - min cena dla Mk3\n'
                      '2 - max cena dla Mk3\n'
                      '3 - min cena dla E60\n'
                      '4 - max cena dla E60\n'
                      '5 - min przebieg dla Mk3\n'
                      '6 - max przebieg dla Mk3\n'
                      '7 - min przebieg dla E60\n'
                      '8 - max przebieg dla E60\n'
                      'q - aby wyjsc\n:')
        if wybor=='1':
            min_price('Mk3 (2010-)')
        elif wybor=='2':
            max_price('Mk3 (2010-)')
        elif wybor=='3':
            min_price('E60 (2003-2010)')
        elif wybor=='4':
            max_price('E60 (2003-2010)')
        elif wybor=='5':
            min_przebieg('Mk3 (2010-)')
        elif wybor=='6':
            max_przebieg('Mk3 (2010-)')
        elif wybor=='7':
            min_przebieg('E60 (2003-2010)')
        elif wybor=='8':
            max_przebieg('E60 (2003-2010)')

