import psycopg2

# Connecting to "chinook" database:
connection = psycopg2.connect(database="chinook")

# Building a cursor object of the database:
cursor = connection.cursor()

# Query 1 - Select all records from the "Artist" table:
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table:
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" from the "Artist" table:
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table:
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the albums with "ArtistId" #51 from the "Album" table:
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks from the "Track" table with composer = "Queen":
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Fetching the results (multiple):
results = cursor.fetchall()

# Fetching the result (single):
# results = cursor.fetchone()

# Closing the connection:
connection.close()

# Printing results:
for result in results:
    print(result)
