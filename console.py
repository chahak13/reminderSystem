from login import login, register
from reminder import addReminder

currentUser = None

def userFunctions(currentUser):
    # print("User Functions")
    print("****************************************")
    print("Logged in as : ",currentUser.username)
    print("****************************************")
    print("Press 1 to create a new reminder")
    print("Press 2 to Exit")
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
        addReminder(currentUser.userid, type, text, time)

    elif (choice=='2'):
        exit()

def main():
    print("****************************************")
    print("Press 1 to Login.")
    print("Press 2 to Register")
    print("Press 3 to Exit")
    choice = input("Your choice : ")
    print("****************************************")
    if(choice=='1'):
        currentUser = login()
        if (currentUser==None):
            print("****************************************")
            print ("Please enter correct credentials")
            print("****************************************")
        else:
            userFunctions(currentUser)
    elif(choice == '2'):
        currentUser = register()
        if (currentUser==None):
            print("****************************************")
            print ("Please enter proper credentials")
            print("****************************************")
        else:
            print("****************************************")
            print ("Registered successfully")
            print("****************************************")
            userFunctions(currentUser)
    elif (choice=='3'):
        exit()
    else:
        print("Please choose correct option")

if __name__ == '__main__':
    while(True):
        main()
