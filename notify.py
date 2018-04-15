import datetime
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_declarative import Reminder, Base, Notification

def main():
    engine = create_engine('sqlite:///reminderSystem.db')
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    while(True):
        Notification.notify(session)
        time.sleep(60)

if __name__ == '__main__':
    main()
