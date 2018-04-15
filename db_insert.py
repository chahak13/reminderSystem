import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Date, String, Integer, ForeignKey

from db_declarative import User, Base, Reminder

def insertUser(uname, passw, email):
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

    # Insert a Person in the person table
    new_user = User(username=uname, password = passw, userEmail = email)
    session.add(new_user)
    session.commit()
    return True

def insertReminder(userid, type, text, time):
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

    # Insert a Reminder in the Reminder table
    year = int(time.get('year', 2018))
    month = int(time.get('month', 1))
    day = int(time.get('day', 1))
    hour = int(time.get('hour', 12))
    mins = int(time.get('mins', 00))

    new_reminder = Reminder(userID = userid, type = type, text = text, time = datetime.datetime(year, month, day, hour=hour, minute=mins))
    session.add(new_reminder)
    session.commit()
    return True
