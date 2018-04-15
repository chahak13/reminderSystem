import datetime
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    userid = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    userEmail = Column(String(250), nullable=False)
    rating = Column(Integer)
    phoneNumber = Column(String(15))

class Reminder(Base):
    __tablename__ = 'reminder'
    reminderID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('user.userid'))
    type = Column(String(20), nullable=False)
    text = Column(String(20), nullable=False)
    time = Column(DateTime)

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
