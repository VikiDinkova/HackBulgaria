import sqlite3

conn = sqlite3.connect("cinema.db")
c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS Movies(
#              id INTEGER PRIMARY KEY Autoincrement not null,
#              name varchar(255) not null,
#              rating float null
#              )
#              """
#           )

# c.execute("""CREATE TABLE IF NOT EXISTS Projections(
#              id INTEGER PRIMARY KEY Autoincrement not null,
#              movie_id integer not null,
#              type varchar(255) not null,
#              date varchar(255) not null,
#              time varchar(255) null,
#              FOREIGN KEY (movie_id) REFERENCES Movies(id)
#              )
#              """
#           )

# c.execute("""CREATE TABLE IF NOT EXISTS Reservations(
#              id INTEGER PRIMARY KEY Autoincrement not null,
#              username varchar(255) not null,
#              projection_id integer not null,
#              row integer not null,
#              col integer not null,
#              FOREIGN KEY (projection_id) REFERENCES Projections(id)
#              )
#              """
#           )

# c.execute("""INSERT INTO Movies(
#              name,
#              rating
#             )
#             VALUES
#             ("The Hunger Games: Catching Fire", 7.9),
#             ("Wreck-It Ralph", 7.9),
#             ("Her", 8.3)
#         """
#           )

# c.execute("""INSERT INTO Projections(
#              movie_id,
#              type,
#              date,
#              time
#             )
#              VALUES
#              (1,"3D","2014-04-01","19:00"),
#              (1,"2D","2014-04-01","19:00"),
#              (1,"4DX","2014-04-02","21:00"),
#              (3,"2D","2014-04-05","20:20"),
#              (2,"3D","2014-04-02","22:00"),
#              (2,"2D","2014-04-02","19:30")
#              """
#           )

# c.execute("""INSERT INTO Reservations(
#              username,
#              projection_id,
#              row,
#              col
#              )
#              VALUES
#              ("RadoRado",1,2,1),
#              ("RadoRado",1,3,5),
#              ("RadoRado",1,7,8),
#              ("Ivo",3,1,1),
#              ("Ivo",3,1,2),
#              ("Mysterious",5,2,3),
#              ("Mysterious",5,2,4)
#     """)

# conn.commit()


def show_movies():
    print("Current movies:\n")
    c.execute("""SELECT id, name, rating
                 FROM Movies AS m
                 ORDER BY rating
    """)
    return c.fetchall()


def show_movie_projections(movie_id, movie_date):
    c.execute("""SELECT pr.time
                FROM Movies AS m
                JOIN Projections AS pr
                ON m.id = pr.movie_id
                WHERE pr.date = ?
                AND pr.movie_id = ?
        """, (movie_date, movie_id))
    return c.fetchall()


def show_current_movie_projections(movie_id):
    c.execute("""SELECT pr.time
                FROM Movies AS m
                JOIN Projections AS pr
                ON m.id = pr.movie_id
                WHERE pr.movie_id = ?
        """, (movie_id))
    return c.fetchall()


def make_hall():
    b = []
    a = [' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b.append(a)
    for i in range(1, 11):
        b.append([i])
        for j in range(10):
            b[i].append(".")
    return b


def print_hall():
    arr = make_hall()
    for row in arr:
        col = [str(c) for c in row]
        a = ' '.join(col)
        print(a)
    return " "


def in_table(col, row):
    return int(col) <= 10 and int(row) <= 10 and int(col) > 0 and int(row) > 0


def is_seat_taken(col, row, cinema_hall):
    return cinema_hall[int(row)][int(col)] == "X"


def change_status(row, col):
    make_hall()[int(row)][int(col)] = 'X'


def main():
    while True:
        st_stuff = input("> ")
        if st_stuff == "show_movies":
            print(show_movies())
        elif "show_movie_projections" in st_stuff:
            print(show_movie_projections(st_stuff[1], st_stuff[2]))
        elif "make_reservation":
            input("Step 1: (User): Choose name > ")
            input("Step 2: (User): Choose number of tickets >")
            print(show_movies())
            a = input("Step 2 (Movie): Choose a movie>")
            print(show_current_movie_projections(a))
            print("Available seats (marked with a dot):")
            print(print_hall())
            while True:
                try_res = input("Step 4 (Seats): Choose seat 1> ")
                if in_table(try_res[0], try_res[2]):
                    if is_seat_taken(try_res[0], try_res[2], make_hall()):
                        print("This seat is already taken!")
                    else:
                        change_status(try_res[0], try_res[2])
                        print("Your reservation is OK")
                    break
                else:
                    print("Lol...NO!")
        a = input("Step 5 (Confirm - type 'finalize') >")
        if a == "finalize":
            break


if __name__ == '__main__':
    print(main())
