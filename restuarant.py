from review import Review
class Restaurant :
    def __init__(self , name):
        self._name = name
        self.reviews = []

    def name (self):
        return self._name
    
    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews (self):
        return self.reviews
    
    def customers(self):
        unique_customers = set()
        for review in self.reviews:
            unique_customers.add(review.customer())
        return list (unique_customers)
    
restaurant = Restaurant("Delicious Eats")
review1 = Review("Jane", restaurant, 4)
review2 = Review("John", restaurant, 5)

print(f"Restaurant: {restaurant.name()}")
print("Reviews:")
for review in restaurant.get_reviews():
    print(f"Customer: {review.customer()}, Rating: {review.rating()}")
    
print("Customers:")
for customer in restaurant.customers():
    print(customer)