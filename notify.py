import datetime
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

def notify():
    reminderList = session.query(Reminder).all()
    for reminder in reminderList:
        if (reminder.time.minute == datetime.datetime.now().minute):
            print(reminder.text, reminder.time.minute)
            os.system('notify-send "'+reminder.text+'"')
            exit()
    return

def main():
    while(True):
        notify()

if __name__ == '__main__':
    main()
