# Define the Customer class
class Customer:
    # Initialize a class variable to store all customers
    all_customers = []

     # Define the constructor method to set the given name and family name properties
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        # Add the customer to the list of all customers
        Customer.all_customers.append(self)