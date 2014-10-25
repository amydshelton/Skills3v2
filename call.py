

"""
call.py - Telemarketing script that displays the next name 
          and phone number of a Customer to call.

          This script is used to drive promotions for 
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

import sqlite3

DB = None
CONN = None


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime,date


ENGINE = None
Session = None

Base = declarative_base()


# Class definition to store our customer data
class CustomerToCall(Base):

	__tablename__ = 'customers'
	# __mapper_args__ = {'primary_key':'id'}

	# def(self, id=None, first=None, last=None, telephone=None):
	id = Column(Integer, primary_key = True)
	givenname = Column(String, nullable = True)
	surname = Column(String, nullable = True)
	telephone = Column(String, nullable = True)
	called = Column(Date, nullable = True)


	def __str__(self):
		output = "Name: %s, %s\n" % (self.surname, self.givenname)
		output += "Phone: %s" % self.telephone

		return output

# Connect to the Database
def connect_to_db():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///melons.db", echo=False)
    Session = sessionmaker(bind = ENGINE)

    return Session()


# Retrieve the next uncontacted customer record from the database.
# Return the data in a Customer class object.
#
# Remember: Our telemarketers should only be calling customers
#           who have placed orders of 20 melons or more.
def get_next_customer(session):
	# c = Customer()

	customers = session.query(CustomerToCall).all()

	for customer in customers:

		if customer.called == None: 
			return customer
		else:
			continue


def display_next_to_call(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print customer
	print "\n"


# Update the "last called" column for the customer
#   in the database.
def update_customer_called(session, customer):
	todays_date = date.today()
	customer.called = todays_date
	session.commit()


def main():
	session = connect_to_db()

	done = False
	

	while not done:
		customer = get_next_customer(session)

		display_next_to_call(customer)

		print "Mark this customer as called?"
		user_answer = raw_input('(y/n) > ')

		if user_answer.lower() == 'y':
			update_customer_called(session,customer)
		else:
			done = True


if __name__ == '__main__':
	main()