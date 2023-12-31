class Customer:
    all_customers = []

    def __init__(self, given_name: str, family_name: str) -> None:
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []

        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.family_name} {self.given_name}"
    
    def restaurants(self):
        all_restaurants = []
        for review in self.reviews:
            all_restaurants.append(review.__restaurant)
        unique_restaurants = list(set(all_restaurants))
        return unique_restaurants
    
    def add_review(self, restaurant, rating):
        if isinstance(restaurant, Restaurant):
            review = Review(self.given_name, restaurant, rating)
            self.reviews.append(review)
        

    def __repr__(self):
        return f"{self.__class__.__name__}({self.given_name}, {self.family_name})"


class Restaurant:
    all_restaurants = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        all_customers = []
        for review in self.reviews:
            all_customers.append(review.__customer)
        unique_customers = list(set(all_customers))
        return unique_customers

    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"


class Review:
    all_reviews = []
    
    def __init__(self, customer, restaurant, rating: int) -> None:
        self.__customer = customer
        self.__restaurant = restaurant
        self.rating = rating        
        Review.all_reviews.append(self)
        
    @property    
    def customer(self):
        return self.__customer
    
    @property
    def restaurant(self):
        return self.__restaurant
        
    def __repr__(self):
        return f"{self.__class__.__name__}({self.customer}, {self.restaurant}, {self.rating})"


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
            
        
# Define the Restaurant class
class Restaurant:
    # Initialize a class variable to store all restaurants
    all_restaurants = []

    # Define the constructor method to set the name property
    def __init__(self, name):
        self.name = name
        self.reviews = []
        # Add the restaurant to the list of all restaurants
        Restaurant.all_restaurants.append(self)

    # Define a getter method to return the name property
    def name(self):
        return self.name

    # Define a class method to return all restaurants
    @classmethod
    def all(cls):
        return cls.all_restaurants

    # Define a method to return a list of all the reviews for the restaurant
    def reviews(self):
        return self.reviews

    # Define a method to return a list of all customers who have reviewed the restaurant
    def customers(self):
        customers = []
        for review in self.reviews:
            customers.append(review.customer)
        return list(set(customers))

    # Define a method to return the average star rating for the restaurant
    def average_star_rating(self):
        total_rating = 0
        for review in self.reviews:
            total_rating += review.rating
        if len(self.reviews) == 0:
            return "No ratings yet"
        else:
            return total_rating / len(self.reviews)
        
        
# Define the Review class
class Review:
    # Initialize a class variable to store all reviews
    all_reviews = []

    # Define the constructor method to set the customer, restaurant, and rating properties
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.customer.reviews.append(self)
        self.restaurant.reviews.append(self)
        # Add the review to the list of all reviews
        Review.all_reviews.append(self)

    # Define a getter method to return the rating property
    def rating(self):
        return self.rating

    # Define a class method to return all reviews
    @classmethod
    def all(cls):
        return cls.all_reviews

    # Define a method to return the customer object for the review
    def customer(self):
        return self.customer

    # Define a method to return the restaurant object for the review
    def restaurant(self):
        return self.restaurant


# Create a customer instance
Annie = Customer("Annie", "Harper")

# Print Annie's family name using the property
print(Annie.family_name)