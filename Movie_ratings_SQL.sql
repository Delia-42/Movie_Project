create database Movie_Ratings_Project; #This where the database was created.
use Movie_Ratings_Project; #This indicates that I will be using the Movie_Ratings_Project

create table movies  #The table and its name was created.  The schema for this table is below:
(id int primary key, title varchar(50), release_year int, genre varchar(20));

insert into movies values #Created values for the movies table.
(1,"The Shawshank Redemption",1994,"Drama"),
(2,"Schindler's List", 1993,"Drama"),
(3,"Pulp Fiction",1994,"Drama"),
(4,"Fight Club",1999,"Drama"),
(5,"The Matrix", 1999,"Action"),
(6,"Se7en",1995,"Drama"),
(7,"The Silence of the Lambs",1991,"Drama"),
(8,"Back to the Future",1985,"Sci-Fi"),
(9,"Psycho",1960,"Horror"),
(10,"Leon: The Professional",1994,"Action"),
(11,"The Lion King",1994,"Drama"),
(12,"Gladiator",2000,"Action"),
(13,"Rear Window",1954,"Mystery"),
(14,"Alien",1979,"Sci-Fi"),
(15,"Indiana Jones and the Raiders of the Lost Ark",1981,"Action"),
(16,"The Shining",1980,"Horror"),
(17,"Aliens",1986,"Sci-Fi"),
(18,"Braveheart",1995,"Drama"),
(19,"Inglourious Basterds",2009,"Drama"),
(20,"Vertigo",1958,"Mystery"),
(21,"Indiana Jones and the Last Crusade",1989,"Action"),
(22,"The Wolf of Wall Street",2013,"Comedy"),
(23,"Pan's Labyrinth",2006,"Drama"),
(24,"The Sixth Sense",1999,"Mystery"),
(25,"A Beautiful Mind",2001,"Drama"),
(26,"The Great Escape",1963,"Adventure"),
(27,"Jurassic Park",1993,"Adventure"),
(28,"Kill Bill Vol.1",2003,"Action"),
(29,"Finding Nemo",2003,"Adventure"),
(30,"V for Vendetta",2005,"Drama"),
(31,"The Thing",1982,"Sci-Fi"),
(32,"Dial M for Murder",1954,"Mystery"),
(33,"Gone Girl",2014,"Drama"),
(34,"Jaws",1975,"Horror"),
(35,"Rocky",1976,"Drama"),
(36,"The Terminator",1984,"Sci-Fi"),
(37,"The Wizard of Oz",1939,"Adventure"),
(38,"Groundhog Day",1993,"Comedy"),
(39,"The Exorcist",1973,"Horror"),
(40,"The Sound of Music",1965,"Drama"),
(41,"Dances with Wolves",1990,"Adventure"),
(42,"Predator",1987,"Sci-Fi"),
(43,"The Ring",2002,"Horror"),
(44,"The Blide Side",2009,"Drama"),
(45,"Arachnophobia",1990,"Horror"),
(46,"Scream",1996,"Horror"),
(47,"Anacondas: The Hunt for the Blood Orchid",2004,"Horror"),
(48,"Senior Year",2022,"Comedy"),
(49,"The Goonies",1985,"Adventure"),
(50,"Beetlejuice",1988,"Comedy");

select * from movies; #Selects the entire movie table

select title, release_year from movies
order by release_year; #Sorts the release year in ascending order of each movie.

create table reviewers #Created the table for Reviewers. The schema for this table is below:
(id int primary key, first_name varchar(30), last_name varchar(40)); 

insert into reviewers values
(1,"Laura","Lane"),
(2,"Care","Bear"),
(3,"Jonah","Beach"),
(4,"Grass", "Orchid"),
(5,"Mother","Goose"),
(6,"Woody","Blanket"),
(7,"Peachy","Curtain"),
(8,"Monica","Curts"),
(9,"Laney","Road"),
(10,"Ronnie","Backyard"),
(11,"Shark","Tanky"),
(12,"Branky","Stewart"),
(13, "Snow","White"),
(14,"Mickey","Mouse"),
(15,"Michael","Myers"),
(16,"Annabella","Sky"),
(17,"Pinocchio","Nose"),
(18,"Sneezy","Gnome"),
(19,"Benny","Were"),
(20,"LaLa","Paloosa"),
(21,"Papier","Blanc"),
(22,"Vento","Morgan"),
(23,"Drake","Memento"),
(24,"Slider","Mongi"),
(25,"Deja","Fire"),
(26,"Maddie","Monroe"),
(27,"Kyle","South"),
(28,"Kenny","North"),
(29,"Cartman","West"),
(30,"Tweak","East"),
(31,"Toni","Self"),
(32,"Maya","May"),
(33,"Lynn","Ever"),
(34,"William","Law"),
(35,"Bellatrix","Lestrange"),
(36,"Malfoy","Slytherin"),
(37,"Selena","Green"),
(38,"Serena","Waterford"),
(39,"June","Bug"),
(40,"Paul","Hollywood"),
(41,"Mary","Berry"),
(42,"Jingle","Bells"),
(43,"Rascal","Pascal"),
(44,"Diablo","Land"),
(45,"Dobryana","Essie"),
(46,"Peter","Rabbit"),
(47,"Ceja","Beach"),
(48,"Koala","Said"),
(49,"Jay","Bean"),
(50,"Frodo","Hobbit");

select * from reviewers;
