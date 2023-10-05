# crud_operations.py
from sqlalchemy.orm import sessionmaker
from models import engine, Customer, Interaction, Review

Session = sessionmaker(bind=engine)

def create_customer(name):
    session = Session()
    customer = Customer(name=name)
    session.add(customer)
    session.commit()
    session.close()

def get_customers():
    session = Session()
    customers = session.query(Customer).all()
    session.close()
    return customers

def get_customer_by_id(customer_id):
    session = Session()
    customer = session.query(Customer).filter_by(id=customer_id).first()
    session.close()
    return customer

def update_customer(customer_id, new_name):
    session = Session()
    customer = session.query(Customer).filter_by(id=customer_id).first()
    customer.name = new_name
    session.commit()
    session.close()

def delete_customer(customer_id):
    session = Session()
    customer = session.query(Customer).filter_by(id=customer_id).first()
    session.delete(customer)
    session.commit()
    session.close()
