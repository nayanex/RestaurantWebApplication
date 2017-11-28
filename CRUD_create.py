from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

''' 
sessionmaker object. This establishes a link of communication 
between our code executions and the engine we just created.
'''
DBSession = sessionmaker(bind = engine)

'''
In order to create, read, update or delete information on our database, SQLAlchemy executes database
operations via an interface. It's called a session. A session allows us to write down all the commands
we want to execute, but not send them to the database until we call a commit.
'''
session = DBSession()

'''
Here, I'll show you what I mean. I'm going to create an instance of a DBSession and call it session
for short. From now on, when I want to make a change to my database, I can do it just by calling a method
from within session.
'''
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)

'''
The DBSession object gives me a staging zone for all of the objects loaded into a database 
session object. Any change made to the objects in the session won't be persisted into the 
database until I call session.commit.
'''
session.commit()

session.query(Restaurant).all

cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella",
course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)

session.add(cheesepizza)
session.commit()

session.query(MenuItem).all()
