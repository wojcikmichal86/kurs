from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Kampania(Base):
    __tablename__ = 'kampanie'
    id = Column(Integer, primary_key=True)
    data = Column(String)
    id_portalu = Column(Integer, ForeignKey('portale.id'))
    rodzaj_api = Column(String)
    campaigns_p = relationship('Portale', back_populates='portals')
    campaigns_o = relationship('Oferty', back_populates='offers')
    def __repr__(self):
        return f'<Kampania(id={self.id}, portal={self.id_portalu})>'

class Portale(Base):
    __tablename__ = 'portale'
    id = Column(Integer, primary_key=True)
    nazwa_portalu = Column(String)
    portals = relationship('Kampania', back_populates='campaigns_p')
    def __repr__(self):
        return f'<Portal(id={self.id}, nazwa={self.nazwa_portalu})>'

class Oferty(Base):
    __tablename__ = 'oferty'
    id = Column(Integer, primary_key=True)
    id_kampanii = Column(Integer, ForeignKey('kampanie.id'))
    id_oferty = Column(String)
    id_sprzedajacego = Column(String)
    lokalizacja = Column(String)
    tytul = Column(String)
    cena = Column(Integer)
    marka = Column(String)
    model = Column(String)
    rok_produkcji = Column(Integer)
    przebieg = Column(Integer)
    pojemnosc = Column(Integer)
    moc = Column(Integer)
    rodzaj_paliwa = Column(String)
    kolor = Column(String)
    uszkodzony = Column(String)
    kraj = Column(String)
    naped = Column(String)
    liczba_miejsc = Column(String)
    offers = relationship('Kampania', back_populates='campaigns_o')
    def __repr__(self):
        return f'<Oferty(id={self.id}, marka={self.marka}, model={self.model}, cena={self.cena})>'