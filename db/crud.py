# https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/
import config 
from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker

print(config.DATABASE_URI)

engine = create_engine(config.DATABASE_URI)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

# engine = create_engine(DATABASE_URI)
recreate_database()


Session = sessionmaker(bind=engine)
s = Session
s.close_all_sessions()