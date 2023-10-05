import click
from crud_operations import create_customer, get_customers, get_customer_by_id, update_customer, delete_customer

@click.group()
def cli():
    pass

@cli.command()
def create():
    name = click.prompt('Enter customer name')
    create_customer(name)
    print("Customer created successfully!")

@cli.command()
def get():
    customers = get_customers()
    print("Customers:")
    for customer in customers:
        print(f"ID: {customer.id}, Name: {customer.name}")

@cli.command()
def get_by_id():
    customer_id = click.prompt('Enter customer ID', type=int)
    customer = get_customer_by_id(customer_id)
    if customer:
        print(f"ID: {customer.id}, Name: {customer.name}")
    else:
        print("Customer not found.")

@cli.command()
def update():
    customer_id = click.prompt('Enter customer ID to update', type=int)
    new_name = click.prompt('Enter new customer name')
    update_customer(customer_id, new_name)
    print("Customer updated successfully!")

@cli.command()
def delete():
    customer_id = click.prompt('Enter customer ID to delete', type=int)
    delete_customer(customer_id)
    print("Customer deleted successfully!")

if __name__ == '__main__':
    cli()
