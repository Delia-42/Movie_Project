create database Movie_Ratings_Project; #This is how the database was created.
use Movie_Ratings_Project; #This indicates that I will be using the Movie_Ratings_Project database.

create table movies  #This is where the first table and its name were created.  The schema for this table is below:
(id int primary key AUTO_INCREMENT, title varchar(50), release_year int, genre varchar(20)); #The auto increment was used to generate unique ids for the primary key whenever a record is created.

insert into movies (title,release_year,genre) values #This is where values were inputed into the movies table.
("The Shawshank Redemption",1994,"Drama"),
("Schindler's List", 1993,"Drama"),
("Pulp Fiction",1994,"Drama"),
("Fight Club",1999,"Drama"),
("The Matrix", 1999,"Action"),
("Se7en",1995,"Drama"),
("The Silence of the Lambs",1991,"Drama"),
("Back to the Future",1985,"Sci-Fi"),
("Psycho",1960,"Horror"),
("Leon: The Professional",1994,"Action"),
("The Lion King",1994,"Drama"),
("Gladiator",2000,"Action"),
("Rear Window",1954,"Mystery"),
("Alien",1979,"Sci-Fi"),
("Indiana Jones and the Raiders of the Lost Ark",1981,"Action"),
("The Shining",1980,"Horror"),
("Aliens",1986,"Sci-Fi"),
("Braveheart",1995,"Drama"),
("Inglourious Basterds",2009,"Drama"),
("Vertigo",1958,"Mystery"),
("Indiana Jones and the Last Crusade",1989,"Action"),
("The Wolf of Wall Street",2013,"Comedy"),
("Pan's Labyrinth",2006,"Drama"),
("The Sixth Sense",1999,"Mystery"),
("A Beautiful Mind",2001,"Drama"),
("The Great Escape",1963,"Adventure"),
("Jurassic Park",1993,"Adventure"),
("Kill Bill Vol.1",2003,"Action"),
("Finding Nemo",2003,"Adventure"),
("V for Vendetta",2005,"Drama"),
("The Thing",1982,"Sci-Fi"),
("Dial M for Murder",1954,"Mystery"),
("Gone Girl",2014,"Drama"),
("Jaws",1975,"Horror"),
("Rocky",1976,"Drama"),
("The Terminator",1984,"Sci-Fi"),
("The Wizard of Oz",1939,"Adventure"),
("Groundhog Day",1993,"Comedy"),
("The Exorcist",1973,"Horror"),
("The Sound of Music",1965,"Drama"),
("Dances with Wolves",1990,"Adventure"),
("Predator",1987,"Sci-Fi"),
("The Ring",2002,"Horror"),
("The Blide Side",2009,"Drama"),
("Arachnophobia",1990,"Horror"),
("Scream",1996,"Horror"),
("Anacondas: The Hunt for the Blood Orchid",2004,"Horror"),
("Senior Year",2022,"Comedy"),
("The Goonies",1985,"Adventure"),
("Beetlejuice",1988,"Comedy");

# The next two select statements were used simply to briefly explore and test the movies table.

select * from movies; # I used this select option in order to check and see if the values were actually inputed into the movies table.

select title, release_year from movies
order by release_year; #I used this option to check out the oldest movie in the collection.

create table reviewers #This is where I created the 2nd table for the movies_ratings_project database.  This is the reviewers table.  The schema for this table is below, and as you can see I also used the auto increment option:
(id int primary key AUTO_INCREMENT, first_name varchar(30), last_name varchar(40)); 

insert into reviewers(first_name,last_name) values #This is where I inputed the values for the reviewers table.
("Laura","Lane"),
("Care","Bear"),
("Jonah","Beach"),
("Grass", "Orchid"),
("Mother","Goose"),
("Woody","Blanket"),
("Peachy","Curtain"),
("Monica","Curts"),
("Laney","Road"),
("Ronnie","Backyard"),
("Shark","Tanky"),
("Branky","Stewart"),
("Snow","White"),
("Mickey","Mouse"),
("Michael","Myers"),
("Annabella","Sky"),
("Pinocchio","Nose"),
("Sneezy","Gnome"),
("Benny","Were"),
("LaLa","Paloosa"),
("Papier","Blanc"),
("Vento","Morgan"),
("Drake","Memento"),
("Slider","Mongi"),
("Deja","Fire"),
("Maddie","Monroe"),
("Kyle","South"),
("Kenny","North"),
("Cartman","West"),
("Tweak","East"),
("Toni","Self"),
("Maya","May"),
("Lynn","Ever"),
("William","Law"),
("Bellatrix","Lestrange"),
("Malfoy","Slytherin"),
("Selena","Green"),
("Serena","Waterford"),
("June","Bug"),
("Paul","Hollywood"),
("Mary","Berry"),
("Jingle","Bells"),
("Rascal","Pascal"),
("Diablo","Land"),
("Dobryana","Essie"),
("Peter","Rabbit"),
("Ceja","Beach"),
("Koala","Said"),
("Jay","Bean"),
("Frodo","Hobbit");

# Next as before, I checked to make sure that the values were actually inputed into the reviewers table.

select * from reviewers;

# I then created a third table for the ratings.  In this table you'll see the foreign keys (ids) that will refer to the primary keys in the 1st and 2nd tables.
create table ratings (
    movie_id int not null,
    reviewer_id int not null,
	rating int,
    foreign key (movie_id) references movies(id),
    foreign key (reviewer_id) references reviewers(id)
);

insert into ratings values # Here I have manually inputed values for the id columns and then randomly input ratings for the movies.
(1,1,8),
(2,2,9),
(3,3,8),
(4,4,7),
(5,5,9),
(6,6,7),
(7,7,8),
(8,8,9),
(9,9,9),
(10,10,1),
(11,11,2),
(12,12,3),
(13,13,4),
(14,14,5),
(15,15,6),
(16,16,7),
(17,17,8),
(18,18,9),
(19,19,1),
(20,20,2),
(21,21,3),
(22,22,4),
(23,23,5),
(24,24,6),
(25,25,7),
(26,26,8),
(27,27,9),
(28,28,8),
(29,29,7),
(30,30,6),
(31,31,5),
(32,32,4),
(33,33,3),
(34,34,2),
(35,35,1),
(36,36,2),
(37,37,3),
(38,38,4),
(39,39,5),
(40,40,6),
(41,41,7),
(42,42,8),
(43,43,9),
(44,44,8),
(45,45,9),
(46,46,8),
(47,47,7),
(48,48,6),
(49,49,5),
(50,50,4),
(2,3,7),
(4,6,7),
(6,7,9),
(3,5,9),
(6,8,2),
(2,5,8),
(23,24,5),
(32,45,8),
(45,32,6),
(38,37,2),
(50,47,8),
(32,35,8),
(31,23,4),
(29,32,7),
(14,16,7),
(13,17,8),
(23,32,7),
(33,42,8),
(41,45,9),
(32,6,8),
(29,32,4),
(41,35,8),
(19,24,8),
(17,42,9),
(21,22,5),
(13,15,6),
(14,41,7),
(21,23,8),
(23,14,7),
(14,32,8),
(21,12,9),
(5,43,8),
(7,42,7),
(8,34,7);

# I've once again created a select statement to make sure that the ratings values were input into the table.

select * from ratings;

# Next you'll see select statements that were tested to make sure that the select statements, that are in python, are in working condition.

SELECT title, genre, MAX(rating)
FROM ratings
INNER JOIN movies
ON movies.id = ratings.movie_id
Where genre = "Horror" 
Group By title
ORDER BY rating DESC
LIMIT 3;

SELECT title, genre, MAX(rating)
FROM ratings
INNER JOIN movies
ON movies.id = ratings.movie_id
Where genre = "Drama" 
Group By title
ORDER BY rating DESC
LIMIT 3;

SELECT title, genre, MAX(rating)
FROM ratings
INNER JOIN movies
ON movies.id = ratings.movie_id
Where genre = "Comedy" 
Group By title
ORDER BY rating DESC
LIMIT 3;

SELECT title, genre, MAX(rating)
FROM ratings
INNER JOIN movies
ON movies.id = ratings.movie_id
Where genre = "Adventure" 
Group By title
ORDER BY rating DESC
LIMIT 3;

SELECT title, genre, MAX(rating)
FROM ratings
INNER JOIN movies
ON movies.id = ratings.movie_id
Where genre = "Action" 
Group By title
ORDER BY rating DESC
LIMIT 3;


# The following are miscellaneous checks on the database:

# movies table select statements -

select title, genre from movies where genre = "horror"; #This can be used to see if a movie has been inserted from python in a particular genre.

select * from movies; # This is used to simply check on the movies inputs.

delete from movies where id = 83; #This is used for deleting rows from the movies table.

SELECT MAX(id) from movies; #This is used to check the highest movies id.


# reviewers table select statements - 

select * from reviewers; #This can be used again to see reviewer table inputs.

select * from reviewers #This can be used to pick out users.
where id = 13;


# ratings table select statements - 

select * from ratings; # This used to check on the ratings table inputs.

select * from ratings #This can be used to see how often a movie has been rated
where movie_id = 84;



 








