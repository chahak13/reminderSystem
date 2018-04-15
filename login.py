from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Date, String, Integer, ForeignKey
from db_insert import insertUser
from db_declarative import User, Base

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


def login():
    uname = input("Username : ")
    passw = input("Password : ")
    res = session.query(User).filter(User.username == uname).first()
    return res

def register():
    uname = input("Username : ")
    passw = input("Password : ")
    email = input("Email ID : ")
    res = insertUser(uname, passw, email)
    if(res==True):
        print("User added successfully")
    else:
        print("Couldn't add user")

    new_user = session.query(User).filter(User.username == uname).first()
    return new_user

def main():
    register()

if __name__ == '__main__':
    main()
