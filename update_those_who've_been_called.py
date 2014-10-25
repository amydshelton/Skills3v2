import csv
#from sqlalchemy import update

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime

ENGINE = None
Session = None

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key = True)
    called = Column(Date, nullable = True)


def load_csv(session,filename): 

    with open(filename, 'rb') as csvfile:
        
        lines = csv.reader(csvfile, delimiter = ',')
        next(lines, None)


        for line in lines:
            cust_id = line[0]
            called_date = line[5]
            if called_date == '':
                continue
            else:
                # Get the customer object from the database
                customer = session.query(Customer).get(cust_id)

                if customer:
                    # Update the customer object with the called date
                    called_date = datetime.strptime(called_date,"%m/%d/%Y")
                    customer.called = called_date
                else:
                    print "Could not find customer with id: ", cust_id



        session.commit()

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///melons.db", echo=True)
    Session = sessionmaker(bind = ENGINE)

    return Session()



def main(session):
    load_csv(session,'called_list.csv')

if __name__ == "__main__":
    s= connect()
    main(s)