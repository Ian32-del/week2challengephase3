from review import Review
class Customer :

    all_customers = []
    def __init__(self , given_name , family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self) 
        self.reviews = []

    def change_given_name (self , new_given_name):
        self.given_name = new_given_name

    def change_family_name (self , new_family_name):
        self.family_name = new_family_name

    def given_name (self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
    
    def full_name (self):
        return f"{self .given_name} {self.family_name} "
    
    @classmethod
    def all(cls):

        return cls.all_customers
    
    def restaurants(self):
        reviewed_restaurants = set()
        for review in self.reviews:
            reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)
    
    def add_review(self,restaurant,rating):
        new_review = Review(self,restaurant,rating)
        self.reviews.append(new_review)
        restaurant.add_review(new_review)

    def num_reviews(self):
        return len(self.reviews)
    
    @classmethod
    def find_by_name(cls,name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None
    
    @classmethod
    def find_all_by_given_name(cls,name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name() == name:
                matching_customers.append(customer)
        return matching_customers
        
    
customer1 = Customer("George", "Washington")

all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name())