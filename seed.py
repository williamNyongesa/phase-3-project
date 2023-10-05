# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer, Product, Interaction, Review, Base
from faker import Faker

fake = Faker()
engine = create_engine("sqlite:///my_database.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Generate fake customers
customers = [Customer(name=fake.name()) for _ in range(10)]
session.add_all(customers)
session.commit()

# Generate fake products
products = [Product(name=fake.word(), price=fake.random_int(min=10, max=200)) for _ in range(5)]
session.add_all(products)
session.commit()

# Generate fake interactions and reviews
for customer in customers:
    interaction = Interaction(type=fake.random_element(elements=('Call', 'Meeting', 'Email')),
                              details=fake.text(),
                              customer=customer)
    review = Review(rating=fake.random_element(elements=(1.0, 2.0, 3.0, 4.0, 5.0)),  # List of possible float values
                    details=fake.text(),
                    customer=customer)
    session.add_all([interaction, review])

session.commit()

print("Fake data generated and added to the database.")
