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

    @staticmethod
    def viewReminders(currentUser, session):
        reminderList = session.query(Reminder).filter(Reminder.userID==currentUser.userid).all()
        counter = 1
        for reminder in reminderList:
            print(counter,')', reminder.text)

        return

    @staticmethod
    def authenticateUser():
        '''
        This function authenticates the user at the time of editing reminders by making use of the Authentication class.
        '''
        return

    def addReminder():
        '''
        Add new reminder for the user
        '''
        return

    def editReminder():
        '''
        Edit existing reminders.
        '''
        return

    def editBiometrics():
        '''
        Edit the biometric details present in the Biometrics class.
        '''
        return

    def requestFriend():
        '''
        Request a friend for reminder.
        '''
        return

    def rateFriend():
        '''
        Rate a friend based on their response to a reminder request.
        '''
        return

    def respondToFriend():
        '''
        Respond to a friend who has requested to be reminded about a reminder.
        '''
        return

    def acknowledgeRequest():
        '''
        Acknowledge the request made by a friend.
        '''
        return

    def declineRequest():
        '''
        Decline the request made by a friend.
        '''
        return

    def receiveNotification():
        '''
        Receive notifications from the system.
        '''
        return

    def resoindToNotification():
        '''
        Respond to the notification obtained by receiveNotification method.
        '''
        return


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

    def deleteReminder():
        '''
        Deletes the reminder from the database
        '''
        return

    def updateReminder():
        '''
        Edits and updates the reminders in the database
        '''
        return

    def searchTag():
        '''
        Provides improved functionality of being able to search for a reminder using tags
        '''
        return


class Friend(Base):
    __tablename__ = 'friend'
    friendID = Column(Integer, primary_key=True)
    friendName = Column(String(250), ForeignKey('user.username'))
    friendEmail = Column(String(250), ForeignKey('user.userEmail'))
    friendPhoneNumber = Column(String(15), ForeignKey('user.phoneNumber'))

    def request():
        '''
        Provides the user with functionality to request a people based reminder from a friend
        '''
        return

    def updateRating():
        '''
        Provids the user with functionality to rate the friend on a scale of 1 to 5. 1 indicating poor service and 5 indicating good service.
        '''
        return

class Sensor(Base):
    __tablename__ = 'sensor'
    SensorID = Column(Integer, primary_key=True)
    SensorData = Column(String(15))

    def sense():
        '''
        an absract method to calculate, measure and return sensor data
        '''
        return

class HeartRateSensor(Base):
    __tablename__ = 'heartratesensor'
    SensorID = Column(Integer, primary_key=True)
    heartRate = Column(String(15))

    def sense():
        '''
        Mesure and send heartrate
        '''
        return heartRate

class GPSSensor(Base):
    __tablename__ = 'gpssensor'
    SensorID = Column(Integer, primary_key=True)
    longitude = Column(Integer)
    latitude = Column(Integer)

    def sense():
        '''
        Mesure and send location
        '''
        return (latitude, longitude)

class WeatherAPI(Base):
    __tablename__ = 'weatherapi'
    location = Column(Integer)
    apiKey = Column(String(50), primary_key=True)
    weatherData = Column(String(100))

    def getWeather():
        '''
        This call returns the current weather details, fetched from the WeatherAPI Object
        '''
        return weatherData


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
                os.system('notify-send "'+reminder.text+'"')
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

class Biometrics(Base):
    __tablename__ = 'biometrics'
    userID = Column(Integer, ForeignKey('user.userid'), primary_key=True)
    workhours = Column(Integer)
    heartRate = Column(Integer)
    bedTime = Column(DateTime)
    age = Column(Integer)
    bmi = Column(Integer)

engine = create_engine('sqlite:///reminderSystem.db')
Base.metadata.create_all(engine)
