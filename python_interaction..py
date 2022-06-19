from colorama import Cursor
import mysql.connector            #This is where I imported the connector class from MySql. 

db = mysql.connector.connect(     # Here, I accessed the connect method through the connector class, and then passed the connection parameters.
    host="localhost",
    user="root",
    passwd="Thidwick108*",
    database="movie_ratings_project"
)

mycursor = db.cursor()    # Here I created the cursor object (mycursor).
#mycursor = db.cursor(buffered=True)

#The following are functions for select statements that are included in a loop in the movie program.
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

# The following are functions for select statements that are in a loop within a loop.
def H_Ratings():
    mycursor.execute('SELECT title, genre, MAX(rating) FROM ratings INNER JOIN movies ON movies.id = ratings.movie_id Where genre = "Horror" Group By title ORDER BY rating DESC LIMIT 3;')
    for x in mycursor:
        print(x)
    
def D_Ratings():
    mycursor.execute('SELECT title, genre, MAX(rating) FROM ratings INNER JOIN movies ON movies.id = ratings.movie_id Where genre = "Drama" Group By title ORDER BY rating DESC LIMIT 3;')
    for x in mycursor:
        print(x)

def C_Ratings():
    mycursor.execute('SELECT title, genre, MAX(rating) FROM ratings INNER JOIN movies ON movies.id = ratings.movie_id Where genre = "Comedy" Group By title ORDER BY rating DESC LIMIT 3;')
    for x in mycursor:
        print(x)

def AD_Ratings():
    mycursor.execute('SELECT title, genre, MAX(rating) FROM ratings INNER JOIN movies ON movies.id = ratings.movie_id Where genre = "Adventure" Group By title ORDER BY rating DESC LIMIT 3;')
    for x in mycursor:
        print(x)

def AC_Ratings():
    mycursor.execute('SELECT title, genre, MAX(rating) FROM ratings INNER JOIN movies ON movies.id = ratings.movie_id Where genre = "Action" Group By title ORDER BY rating DESC LIMIT 3;')
    for x in mycursor:
        print(x)


# The following are functions for users with ids to rate movies.
def New_Review():
    r_title = input ("Enter the movie name:")
    r_release_year = input("Enter the release year:")
    r_genre = input("Enter the genre:")
    sql = "INSERT INTO movies (title, release_year, genre) VALUES (%s, %s, %s)"
    val = (r_title, r_release_year, r_genre)
    mycursor.execute(sql, val)
    db.commit()
    print("record inserted.")

  

def get_movie_id():
    mycursor.execute("SELECT MAX(id) from movies;")
    for x in mycursor:
        movie_id = int(x[0])
        print(movie_id)
    return movie_id
    
    #for x in mycursor:
    #     m = int(x[0])
     #    print(m)
    #return m
    
    
    

#m = 0

# This is where the program prompts the user to input selections.
def startup():                                  
    while True:                               
        print("Ahoy, there! To see a list of movies available, please select a genre to explore. \n Please input a number between 1-5. \n If you would like to see the top rated movies of each genre please input 6. \n If you would like to rate a movie, please input 7. \n Or input 8 if you wish to leave.")  
        print("\t1. Drama")
        print("\t2. Horror")
        print("\t3. Comedy")
        print("\t4. Adventure")
        print("\t5. Action")
        print("\t6. Top_Rated")
        print("\t7. Create_a_Review")
        print("\t8. Quit")
        

        while True:
            try:
                sel = int(input("\nSelection: "))  
            except ValueError:
                print(ValueError)
                print("Please Enter a digit from 1-6:")
            else:
                break  # The following refers to defined functions from the top of the program.
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
            x = input("To check out the top 3 rated movies in Horror, input the value A. \n To check out the top 3 rated movies in Drama, input B.\n  To check out the top 3 rated movies in Comedy, input C. \n To check out the top 3 rated movies in Adventure, input D. \n  To check out the top 3 rated Action movies, input E \n To return back to the main menu, input Q.")
            if x == "A":          #This is the loop within a loop that also refers to defined functions up top.                  
                H_Ratings()
            if x == "B":
                D_Ratings()
            if x == "C":
                C_Ratings()
            if x == "D":
                AC_Ratings()
            if x == "E":
                AD_Ratings()
            if x == "Q":
                break      

        elif sel == 7:  # The following also refers to defined functions from earlier in the program.
            New_Review()
            get_movie_id()
            r_reviewer_id = int(input("Please enter your user ID:"))
            r_rating = input("Enter rating:")    
            sql1 = "INSERT INTO ratings(movie_id, reviewer_id, rating) VALUES (%s, %s, %s)"
            val2 = (movie_id, r_reviewer_id, r_rating)
            movie_id = int(movie_id) # The error states that 'movie_id' is referenced before assignment.
            mycursor.execute(sql1, val2)
            db.commit()
        elif sel == 8:
            print("I hope you've enjoyed your exploration! Have a good day!") 
            break                               
        else:
            print("Sorry!  That input is not recognized")

startup() 