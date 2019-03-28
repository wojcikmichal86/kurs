from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from homework_models import Base

# wskazanie gdzie tworzymy bazę
engine = create_engine('sqlite:///homework.db')

# utworzenie struktury
Base.metadata.create_all(engine)

# utworzenie obiektu sesji
Session = sessionmaker(bind=engine)