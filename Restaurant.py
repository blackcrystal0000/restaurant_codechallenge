class Customer:
    all_customers = []

    def __init__(self, given_name: str, family_name: str) -> None:
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []

        Customer.all_customers.append(self)

    # def given_name(self):
    #     return self.given_name

    # def family_name(self):
    #     return self.family_name

    def full_name(self):
        return f"{self.family_name} {self.given_name}"
    
    def restaurants(self):
        all_restaurants = []
        for review in self.reviews:
            all_restaurants.append(review.__restaurant)
        unique_restaurants = list(set(all_restaurants))
        return unique_restaurants
    
    def add_review(self, restaurant, rating):
        # if isinstance(restaurant, Restaurant):
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

    # def name(self):
    #     return self.name

    # def reviews(self):
    #     return self.reviews

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


