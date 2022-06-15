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
        if sel == 1:                            # if-else statement checks for each possible selection
            Q_Drama()                    # runs the insert_emp() function defined above
        """elif sel == 2:
            Q_horror()
        elif sel == 3:
            Q_comedy()
        elif sel == 4:
            Q_adventure()
        elif sel == 5:
            Q_action()
        elif sel == 6:
            print("Thank you! Have a good day!")
            break                               # immediately break the loop
        else:
            print("Please make a valid input.")"""

startup() # This will run when the program starts