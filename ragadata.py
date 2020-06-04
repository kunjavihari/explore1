
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()


class raga(Base):
    __tablename__ = 'raga'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    thaat = Column(String(30), nullable=True)
    preferredtime = Column(String(30), nullable=True, default='N/A')
    Aroh = Column(String(30),nullable=True)
    Avroh = Column(String(30),nullable=True)

    def __repr__(self):
        return 'raga' + str(self.id)
