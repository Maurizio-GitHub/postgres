# We no longer need the Table class, as we are not going to create tables:
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

# With ORM we will be creating Python classes subclassing the declarative_base:
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database:
db = create_engine("postgresql:///chinook")

# The 'base' class grabs the metadata produced by our database table schema.
# It creates a subclass to map everything back to us into the 'base' variable:
base = declarative_base()


# Creating a class-based model for the "Artist" table:
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# Create a class-based model for the "Album" table:
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# Create a class-based model for the "Track" table:
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# Instead of connecting to the database directly, we will ask for a session!
# Creating a new instance of sessionmaker, pointing to our engine, the db:
Session = sessionmaker(db)

# Opening an actual session by calling the Session() subclass defined above:
session = Session()

# Creating the database using the 'declarative_base' subclass:
base.metadata.create_all(db)

# Query 1 - Select all records from the "Artist" table:

# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - Select only the "Name" column from the "Artist" table:

# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - Select only "Queen" from the "Artist" table:

# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table:

# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - Select only the albums with "ArtistId" #51 from the "Album" table:

# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - Select all tracks from "Track" table with composer = "Queen":
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
