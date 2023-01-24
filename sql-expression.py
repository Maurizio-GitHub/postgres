# Import Classes:
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Executing the instructions from our localhost, "chinook" db:
db = create_engine("postgresql:///chinook")

# MetaData contains a collection of our table objects,
# as well as the associated data within those objects:
meta = MetaData(db)

# Creating the variable for "Artist" table:
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# Creating the variable for "Album" table:
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# Create the variable for "Track" table:
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# Making the connection.
# It saves our connection to the database into a variable called 'connection':
with db.connect() as connection:

    # Query 1 - Select all records from the "Artist" table:
    # query_1 = artist_table.select()

    # Query 2 - Select only the "Name" column from the "Artist" table:
    # query_2 = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - Select only 'Queen' from the "Artist" table:
    # query_3 = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - Select only by 'ArtistId' #51 from the "Artist" table:
    # query_4 = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - Select only albums with 'ArtistId' #51 from the "Album" table:
    # query_5 = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - Select all tracks from "Track" table with composer = "Queen":
    query_6 = track_table.select().where(track_table.c.Composer == "Queen")

    # The query results are stored into a variable called "results".
    # For each result in our results list, we print the result:
    results = connection.execute(query_6)
    for result in results:
        print(result)
