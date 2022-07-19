import pandas as pd               # This is where I imported pandas for a clearer table.
from colorama import Cursor
import mysql.connector            # This is where I imported the connector class from MySql. 

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
        print(x[0])

def Q_Horror():
    mycursor.execute('select title, genre from movies where genre = "horror";')
    for x in mycursor:
        print(x[0])

def Q_Comedy():
    mycursor.execute('select title, genre from movies where genre = "comedy";')
    for x in mycursor:
        print(x[0])

def Q_Adventure():
    mycursor.execute('select title, genre from movies where genre = "adventure";')
    for x in mycursor:
        print(x[0])

def Q_Action():
    mycursor.execute('select title, genre from movies where genre = "action";')
    for x in mycursor:
        print(x[0])

# The following are functions for select statements that are in a loop within a loop.
def H_Ratings():
    mycursor.execute('SELECT title, genre, AVG(rating) FROM ratings INNER JOIN movies ON movies.id = ratings.movie_id Where genre = "Horror" Group By title ORDER BY AVG(rating) DESC LIMIT 4;')
    for x in mycursor:
        x = pd.DataFrame(mycursor, columns=['Title', 'Genre', 'Rating']) 
        print(x)
    
def D_Ratings():
    mycursor.execute('SELECT title, genre, AVG(rating) FROM ratings INNER JOIN movies ON movies.id = ratings.movie_id Where genre = "Drama" Group By title ORDER BY AVG(rating) DESC LIMIT 4;')
    for x in mycursor:
        x = pd.DataFrame(mycursor, columns=['Title', 'Genre', 'Rating']) 
        print(x)

def C_Ratings():
    mycursor.execute('SELECT title, genre, AVG(rating) FROM ratings INNER JOIN movies ON movies.id = ratings.movie_id Where genre = "Comedy" Group By title ORDER BY AVG(rating) DESC LIMIT 4;')
    for x in mycursor:
        x = pd.DataFrame(mycursor, columns=['Title', 'Genre', 'Rating']) 
        print(x)

def AD_Ratings():
    mycursor.execute('SELECT title, genre, AVG(rating) FROM ratings INNER JOIN movies ON movies.id = ratings.movie_id Where genre = "Adventure" Group By title ORDER BY AVG(rating) DESC LIMIT 4;')
    for x in mycursor:
        x = pd.DataFrame(mycursor, columns=['Title', 'Genre', 'Rating']) 
        print(x)

def AC_Ratings():
    mycursor.execute('SELECT title, genre, AVG(rating) FROM ratings INNER JOIN movies ON movies.id = ratings.movie_id Where genre = "Action" Group By title ORDER BY AVG(rating) DESC LIMIT 4;')
    for x in mycursor:
        x = pd.DataFrame(mycursor, columns=['Title', 'Genre', 'Rating']) 
        print(x)


# The following are functions for users with ids to rate movies and to delete their ratings.
def New_Review():
    r_title = input ("Enter the movie name:")
    r_release_year = input("Enter the release year:")
    r_genre = input("Enter the genre:")
    sql = "INSERT INTO movies (title, release_year, genre) VALUES (%s, %s, %s)"  
    val = (r_title, r_release_year, r_genre)
    mycursor.execute(sql, val)
    db.commit()
    print("Movie added.")

def New_Rating():
            movie_id = mycursor.lastrowid
            movie_id = int(movie_id)
            r_reviewer_id = int(input("Please enter your user ID:\n"))
            r_rating = input("Enter rating:\n")    
            sql1 = "INSERT INTO ratings(movie_id, reviewer_id, rating) VALUES (%s, %s, %s)"
            val2 = (movie_id, r_reviewer_id, r_rating)       
            mycursor.execute(sql1, val2)
            db.commit()
            print("Rating added")  

def Update_Movie():
    title_to_update = input("Please enter the new movie title: ")
    title_update = input("Please insert movie id: ")
    mycursor.execute("Update movies SET title=%s where id=%s", (title_to_update, title_update))
    db.commit()
    print("Movie Updated")
        
    
def Delete_Movie_ID():
    mycursor.execute('delete from ratings order by movie_id desc limit 1;')
    db.commit()
    mycursor.execute('delete from movies order by id desc limit 1;')
    db.commit()
    print("Rating deleted")
    
# This is where the program prompts the user to input selections.
def startup():                                  
    while True:                               
        print("\n \n Ahoy, there! To see a list of movies in our collection, please select a genre by inputing a number between 1 and 5. \n \n If you would like to see the top rated movies of each genre please input 6. \n \n If you would like to rate a movie, please input 7. \n \n If you would like to update a movie title, input 8. \n\n If you would like to delete your recent rating, please input 9. \n \n Or input 10 if you wish to leave.\n \n")  
        print("\t1. Drama")
        print("\t2. Horror")
        print("\t3. Comedy")
        print("\t4. Adventure")
        print("\t5. Action")
        print("\t6. Top_Rated")
        print("\t7. Create_a_Review")
        print("\t8. Update_Review")
        print("\t9. Delete_Review")
        print("\t10. Leave")
        

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
            x = input("\n To check out the top 3 rated movies in Horror, input the value A. \n \n To check out the top 3 rated movies in Drama, input B.\n \n To check out the top 3 rated movies in Comedy, input C. \n \n To check out the top 3 rated movies in Adventure, input D. \n \n To check out the top 3 rated movies in Action, input E \n \n")
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
                 

        elif sel == 7:  # The following also refers to defined functions from earlier in the program.
            New_Review()
            New_Rating()
        elif sel == 8:
            Update_Movie()
        elif sel == 9:
            Delete_Movie_ID()
        elif sel == 10:
            print("\nI hope you've enjoyed your rating experience! Have a good day!\n") 
            break                               
        else:
            print("Sorry!  That input is not recognized")

startup() 