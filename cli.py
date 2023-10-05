# cli.py
import click
from crud_operations import create_customer, get_customers, get_customer_by_id, update_customer, delete_customer

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def create(name):
    create_customer(name)
    print("Customer created successfully!")

@cli.command()
def get():
    customers = get_customers()
    print("Customers:")
    for customer in customers:
        print(f"ID: {customer.id}, Name: {customer.name}")

@cli.command()
@click.argument('customer_id', type=int)
def get_by_id(customer_id):
    customer = get_customer_by_id(customer_id)
    if customer:
        print(f"ID: {customer.id}, Name: {customer.name}")
    else:
        print("Customer not found.")

@cli.command()
@click.argument('customer_id', type=int)
@click.argument('new_name')
def update(customer_id, new_name):
    update_customer(customer_id, new_name)
    print("Customer updated successfully!")

@cli.command()
@click.argument('customer_id', type=int)
def delete(customer_id):
    delete_customer(customer_id)
    print("Customer deleted successfully!")

if __name__ == '__main__':
    cli()
