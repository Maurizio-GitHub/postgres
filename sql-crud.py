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
session.add(ada_lovelace)
session.add(alan_turing)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_berners_lee)
session.add(maurizio_loffredo)

# Committing our session to the database:
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
