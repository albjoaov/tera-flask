from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    # foto_perfil = Column(String)  # s3.aws.com/nome_do_bucket/nome-da-imagem.jpg

    def __repr__(self):
        # return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)
        return f"<User(name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}')>"
