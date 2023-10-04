from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine("sqlite:///my_database.db")

# Define the intermediary table for the many-to-many relationship
customer_product = Table('customer_product', Base.metadata,
    Column('customer_id', Integer, ForeignKey('customers.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    interactions = relationship('Interaction', back_populates='customer')
    reviews = relationship('Review', back_populates='customer')
    products = relationship('Product', secondary=customer_product, back_populates='customers')

class Interaction(Base):
    __tablename__ = 'interactions'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    details = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship('Customer', back_populates='interactions')

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    rating = Column(Float)
    details = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship('Customer', back_populates='reviews')

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    customers = relationship('Customer', secondary=customer_product, back_populates='products')

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example Usage:
    customer1 = Customer(name="John Doe")
    customer2 = Customer(name="Jane Smith")

    product1 = Product(name="Product A", price=50.0)
    product2 = Product(name="Product B", price=75.0)

    customer1.products.append(product1)
    customer1.products.append(product2)
    customer2.products.append(product2)

    interaction1 = Interaction(type="Call", details="Discussing new products", customer=customer1)
    interaction2 = Interaction(type="Meeting", details="Sales presentation", customer=customer2)

    review1 = Review(rating=4.5, details="Great product!", customer=customer1)
    review2 = Review(rating=3.8, details="Satisfied with the service", customer=customer2)

    session.add_all([customer1, customer2, product1, product2, interaction1, interaction2, review1, review2])
    session.commit()

    # Querying Example:
    print("Customer 1 Interactions:")
    for interaction in customer1.interactions:
        print(interaction.type, interaction.details)

    print("Customer 1 Reviews:")
    for review in customer1.reviews:
        print(f"Rating: {review.rating}, Details: {review.details}")

    print("Customer 1 Products:")
    for product in customer1.products:
        print(product.name)

    print("Product 2 Customers:")
    for customer in product2.customers:
        print(customer.name)
