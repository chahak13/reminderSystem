import datetime
import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
# from db_insert import insertUser, insertReminder

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    userid = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    userEmail = Column(String(250), nullable=False)
    rating = Column(Integer)
    phoneNumber = Column(String(15))

    @staticmethod
    def login(session):
        uname = input("Username : ")
        passw = input("Password : ")
        res = session.query(User).filter(User.username == uname).first()
        return res

    @staticmethod
    def register(session):
        uname = input("Username : ")
        passw = input("Password : ")
        email = input("Email ID : ")

        new_user = User(username=uname, password = passw, userEmail = email)
        session.add(new_user)
        session.commit()
        # return True

        new_user = session.query(User).filter(User.username == uname).first()
        return new_user


class Reminder(Base):
    __tablename__ = 'reminder'
    reminderID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('user.userid'))
    type = Column(String(20), nullable=False)
    text = Column(String(20), nullable=False)
    time = Column(DateTime)

    @staticmethod
    def addReminder(session, userid, type, text, time):
        # res = insertReminder(userid, type, text, time)
        year = int(time.get('year', 2018))
        month = int(time.get('month', 1))
        day = int(time.get('day', 1))
        hour = int(time.get('hour', 12))
        mins = int(time.get('mins', 00))

        new_reminder = Reminder(userID = userid, type = type, text = text, time = datetime.datetime(year, month, day, hour=hour, minute=mins))
        session.add(new_reminder)
        session.commit()

        # if (res==True):
        print("****************************************")
        print("Reminder added successfully")
        # else:
        #     print("****************************************")
        #     print("Couldn't add reminder")

        return


class Friend(Base):
    __tablename__ = 'friend'
    friendID = Column(Integer, primary_key=True)
    friendName = Column(String(250), ForeignKey('user.username'))
    friendEmail = Column(String(250), ForeignKey('user.userEmail'))
    friendPhoneNumber = Column(String(15), ForeignKey('user.phoneNumber'))

class Notification(Base):
    __tablename__ = 'notification'
    reminderID = Column(Integer, ForeignKey('reminder.reminderID'), primary_key=True)
    timeStamp = Column(DateTime, default=datetime.datetime.utcnow)
    seenTime = Column(DateTime, primary_key=True)

    @staticmethod
    def notify(session):
        reminderList = session.query(Reminder).all()
        for reminder in reminderList:
            if (reminder.time.hour == datetime.datetime.now().hour and reminder.time.minute == datetime.datetime.now().minute):
                # print(reminder.text, reminder.time.minute)
                os.system('notify-send "'+reminder.text+'"')
                # exit()
        return


class Dispatcher(Base):
    __tablename__ = 'dispatcher'
    userID = Column(Integer, ForeignKey('user.userid'), primary_key=True)
    messages = Column(String(5000))
    callLogs = Column(String(1000))
    mails = Column(String(5000))

class Authentication(Base):
    __tablename__ = 'authentication'
    userID = Column(Integer, ForeignKey('user.userid'), primary_key=True)
    authType = Column(String(50))
    credentials = Column(String(250))

engine = create_engine('sqlite:///reminderSystem.db')
Base.metadata.create_all(engine)
