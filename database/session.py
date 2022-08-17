# import sys
#
# sys.path.insert(0, "../")

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.User import User

load_dotenv()
DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_NAME = os.environ['DB_NAME']

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# User.metadata.create_all(engine)
#
# ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# session.add(ed_user)
# session.commit()

our_user = session.query(User).filter_by(name='ed').first()
print(our_user)

# INSERT INTO users (id, name, fullname, nickname) values ('ed', 'Ed Jones', 'edsnickname')
# INSERT INTO users (name, fullname, nickname) VALUES (%(name)s, %(fullname)s, %(nickname)s)
