from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Date, String, Integer, ForeignKey
from db_insert import insertReminder
from db_declarative import Reminder, Base

engine = create_engine('sqlite:///reminderSystem.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

def addReminder(userid, type, text, time):
    res = insertReminder(userid, type, text, time)

    if (res==True):
        print("****************************************")
        print("Reminder added successfully")
    else:
        print("****************************************")
        print("Couldn't add reminder")

    return
