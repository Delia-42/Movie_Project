import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Thidwick108*",
    database="movie_ratings_project"
)
mycursor = db.cursor()
def Q_Drama():
    mycursor.execute('select title, genre from movies where genre = "drama";')
    for x in mycursor:
        print(x)

def Q_Horror():
    mycursor.execute('select title, genre from movies where genre = "horror";')
    for x in mycursor:
        print(x)

def Q_Comedy():
    mycursor.execute('select title, genre from movies where genre = "comedy";')
    for x in mycursor:
        print(x)

def Q_Adventure():
    mycursor.execute('select title, genre from movies where genre = "adventure";')
    for x in mycursor:
        print(x)

def Q_Action():
    mycursor.execute('select title, genre from movies where genre = "action";')
    for x in mycursor:
        print(x)






def startup():                                  # the startup function is called below so that it can run
    while True:                                 # this will loop infinitely because the condition is always True
        print("Ahoy, there! Which movie genre are you wanting to explore?")  # create a menu to give the user options
        print("\t1. Drama")
        print("\t2. Horror")
        print("\t3. Comedy")
        print("\t4. Adventure")
        print("\t5. Action")
        print("\t6. Quit")
        # We want to check for an error if the user inputs a non-integer value
        while True:
            try:
                sel = int(input("\nSelection: "))       # take the user input for the selection
            except ValueError:
                print(ValueError)
                print("Please Enter a digit from 1-6:")
            else:
                break
        if sel == 1:                            
            Q_Drama()                    
        elif sel == 2:
            Q_Horror()
        elif sel == 3:
            Q_Comedy()
        elif sel == 4:
            Q_Adventure()
        elif sel == 5:
            Q_Action()
        elif sel == 6:
            print("I hope you've enjoyed your exploration! Have a good day!")
            break                               # immediately break the loop
        else:
            print("Please make a valid input.")

startup() # This will run when the program starts