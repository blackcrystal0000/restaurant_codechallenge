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

        # Define a getter method to return the given name property
    def given_name(self):
        return self.given_name
    
    # Define a getter method to return the family name property
    def family_name(self):
        return self.family_name
    
    # Define a method to return the full name of the customer in Western style
    def full_name(self):
        return f'{self.family_name} {self.given_name}'

        # Define a method to return a string representation of the class
    def __repr__(self):
        return f"{self.__class__.__name__}({self.given_name}, {self.family_name})"

    # Define a class method to return all customers
    @classmethod
    def all(cls):
        return cls.all_customers

         # Define a method to return a list of all the restaurants reviewed by the customer
    def restaurants(self):
        reviewed_restaurants = [] 
        for review in self.reviews:
            reviewed_restaurants.append(review.restaurant)
        return list(set(reviewed_restaurants))

    # Define a method to return the total number of reviews written by the customer
    def num_reviews(self):
        return len(self.reviews)

    # Define a method to add a review for a restaurant to the customer's list of reviews
    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)

         # Define a class method to find a customer by their full name
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all():
            if customer.full_name() == name:
                return customer
        return "No customer found with that name"

         # Define a class method to find all customers with a given given_name
    @classmethod
    def find_all_by_given_name(cls, name):
        customers_with_given_name = []
        for customer in cls.all():
            if customer.given_name == name:
                customers_with_given_name.append(customer)
        return customers_with_given_name