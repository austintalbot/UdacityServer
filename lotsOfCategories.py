from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database, create_database
from database_setup import Category, CategoryItem, User, Base

engine = create_engine(
    'postgresql+psycopg2://postgres:none@localhost:5432/Catalog')
APPLICATION_NAME = "Austin Talbot - Catalog APP"
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
print('database connected')

# # Clear database

# # Bind the engine to the metadata of the Base class so that the
# # declaratives can be accessed through a DBSession instance

# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# # A DBSession() instance establishes all conversations with the database
# # and represents a "staging zone" for all the objects loaded into the
# # database session object. Any change made against the objects in the
# # session won't be persisted into the database until you call
# # session.commit(). If you're not happy about the changes, you can
# # revert all of them back to the last commit by calling
# # session.rollback()
# session = DBSession()

# Create dummy user
user1 = User(
    name="Austin Talbot",
    email="austintalbot@gmail.com",
    picture="""https://scontent.xx.fbcdn.net/v/t1.0-1/p100x100/15285089_10153841678546685_94009395283824576_n.jpg?_nc_cat=107&oh=7740995f119567ca1c06be0243939797&oe=5C41F878"""
)
session.add(user1)
session.commit()

# Items for Super Cars
category1 = Category(name="Super Cars", user_id=1)
session.add(category1)
session.commit()

item1 = CategoryItem(name="La Ferrari", user_id=1, category=category1)
session.add(item1)
session.commit()

item2 = CategoryItem(name="Chiron", user_id=1, category=category1)
session.add(item2)
session.commit()

item3 = CategoryItem(name="918 Porsche", user_id=1, category=category1)
session.add(item3)
session.commit()

# Items for Strings
category2 = Category(name="Muscle Cars", user_id=1)
session.add(category1)
session.commit()

item1 = CategoryItem(name="Camaro", user_id=1, category=category2)
session.add(item1)
session.commit()

item2 = CategoryItem(name="Mustang", user_id=1, category=category2)
session.add(item2)
session.commit()

item3 = CategoryItem(name="Corvette", user_id=1, category=category2)
session.add(item3)
session.commit()

item4 = CategoryItem(name="Charger", user_id=1, category=category2)
session.add(item4)
session.commit()

# Items for Strings
category3 = Category(name="Trucks", user_id=1)
session.add(category1)
session.commit()

item1 = CategoryItem(name="F150", user_id=1, category=category3)
session.add(item1)
session.commit()

item2 = CategoryItem(name="Sierra", user_id=1, category=category3)
session.add(item2)
session.commit()

item3 = CategoryItem(name="Tundra", user_id=1, category=category3)
session.add(item3)
session.commit()

categories = session.query(Category).all()

for category in categories:
    print(("Category: " + category.name))
