import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_declarative import Base, User, Reminder, Notification

def userFunctions(currentUser, session):
    print("****************************************")
    print("Logged in as : ",currentUser.username)
    print("****************************************")
    print("Press 1 to create a new reminder")
    print("Press 2 to view all reminders")
    print("Press 3 to Exit")
    choice = input("Your choice : ")
    print("****************************************")

    if (choice=='1'):
        type = input("Enter reminder type : ")
        text = input("Enter reminder text : ")
        time = {}
        time['hour'] = input("Hour of reminder (24 hrs format) : ")
        time['mins'] = input("Minutes past hour of reminder : ")
        time['month'] = input("Month of reminder : ")
        time['day'] = input("Day of month reminder : ")
        time['year'] = input("Enter year of reminder : ")
        Reminder.addReminder(session, currentUser.userid, type, text, time)
        userFunctions(currentUser, session)
    elif (choice=='2'):
        User.viewReminders(currentUser, session)
        userFunctions(currentUser, session)
    elif (choice=='3'):
        exit()

def main():

    engine = create_engine('sqlite:///reminderSystem.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    if(os.fork()==0):
        os.system('python3 ./notify.py')

    print("****************************************")
    print("Press 1 to Login.")
    print("Press 2 to Register")
    print("Press 3 to Exit")
    choice = input("Your choice : ")
    print("****************************************")
    if(choice=='1'):
        currentUser = User.login(session)
        if (currentUser==None):
            print("****************************************")
            print ("Please enter correct credentials")
            print("****************************************")
        else:
            userFunctions(currentUser, session)
    elif(choice == '2'):
        currentUser = User.register(session)
        if (currentUser==None):
            print("****************************************")
            print ("Please enter proper credentials")
            print("****************************************")
        else:
            print("****************************************")
            print ("Registered successfully")
            print("****************************************")
            userFunctions(currentUser, session)
    elif (choice=='3'):
        exit()
    else:
        print("Please choose correct option")

if __name__ == '__main__':
    while(True):
        main()
