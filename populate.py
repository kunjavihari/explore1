#used to populate data into our database
import csv
#from ragadata import raga,Base
import pandas
from json import dumps

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

def createThaatTree(record):
    ragalist = []
    myraga = {'raga':record.name, 
                'preferredtime':record.preferredtime}
    ragalist.append(myraga)
    thaatdict = {'thaat':record.thaat,
                    'children': ragalist}
    return thaatdict

def createTree(myragalist,record):
    if (len(myragalist) >0):
        foundmatch=0
        for index in range(len(myragalist)):
            thaatentry = myragalist[index]
            if (thaatentry['thaat'] == record.thaat):
                print(record.thaat)
                ragalist = thaatentry['children']
                myraga = {'raga':record.name,
                        'preferredtime':record.preferredtime}
                ragalist.append(myraga)
                thaatentry['children'] = ragalist
                foundmatch=1
        if(foundmatch==0):
            thaatdict=createThaatTree(record)
            myragalist.append(thaatdict)
    else:
        thaatdict = createThaatTree(record)
        myragalist.append(thaatdict)


def main():
    #use the following code to create data into our data store 
    create = 0
    myragalist = []

    engine = create_engine('sqlite:///raga.db')

    Base.metadata.bind = engine
    
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    all_ragas=session.query(raga).all()
    myragalist=[]
    for everyraga in all_ragas:
        createTree(myragalist,everyraga)
    myragafinal = {'thaat':"ragas" ,
                    'children':myragalist}
    mystr = dumps(myragafinal)

    print(mystr)
    
    
    #read csv
    filename = "/users/kunjukashalikar/Documents/Music/ragalist.csv"
    df = pandas.read_csv(filename)
    print(df)


    if (create ==1):
        #Base = declarative_base()
        engine = create_engine('sqlite:///raga.db')
        Base.metadata.create_all(engine)

        Base.metadata.bind = engine
    
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        for i, j in df.iterrows(): 
            print(j[0])
            new_raga = raga(name=j[0],thaat=j[1],preferredtime=j[2])
            session.add(new_raga)
        session.commit()
    #test function to create a tree structure


if __name__ == "__main__":
    main()