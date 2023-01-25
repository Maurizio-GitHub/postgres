# We no longer need the Table class, as we are not going to create tables:
from sqlalchemy import (
    create_engine, Column, Integer, String
)

# With ORM we will be creating Python classes subclassing the declarative_base:
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database:
db = create_engine("postgresql:///chinook")

# The 'base' class grabs the metadata produced by our database table schema.
# It creates a subclass to map everything back to us into the 'base' variable:
base = declarative_base()


# Creating a class-based model for the "Programmer" table:
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# Instead of connecting to the database directly, we will ask for a session!
# Creating a new instance of sessionmaker, pointing to our engine, the db:
Session = sessionmaker(db)

# Opening an actual session by calling the Session() subclass defined above:
session = Session()

# Creating the database using the 'declarative_base' subclass:
base.metadata.create_all(db)


# Creating records for our Progammer table:
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

maurizio_loffredo = Programmer(
    first_name="Maurizio",
    last_name="Loffredo",
    gender="M",
    nationality="Italian",
    famous_for="Natural Language Programming"
)


# Adding each instance of our programmers to our session:
""" session.add(ada_lovelace)
session.add(alan_turing)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_berners_lee)
session.add(maurizio_loffredo) """


# When we only want one specific record, it is important to add .first().
# Without it, we have to use a for-loop to iterate over the query list,
# even though it will only find a single record using our supplied 'id':
programmer = session.query(Programmer).filter_by(id=7).first()

# Updating a single record:
programmer.famous_for = "World President"

# Updating multiple records; 'session.commit()' needs to be part of the loop:
people = session.query(Programmer)
for person in people:
    if person.gender == "F":
        person.gender = "Female"
    elif person.gender == "M":
        person.gender = "Male"
    else:
        print("Gender not defined")
    session.commit()

# Committing our session to the database:
session.commit()

# Selecting a single record via multiple user entries:
fname = input("Enter a first name: ")
lname = input("Enter a last name: ")
programmer = session.query(Programmer).filter_by(
    first_name=fname, last_name=lname).first()

# Defensive programming:
if programmer is not None:
    print("Found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer has been deleted")
    else:
        print("Programmer not deleted")
else:
    print("No records found")

# Deleting multiple/all records:
programmers = session.query(Programmer)
for programmer in programmers:
    session.delete(programmer)
    session.commit()

# Querying the database to find all Programmers:
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
