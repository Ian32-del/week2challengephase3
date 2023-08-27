class Review :
    all_reviews = []

    def __init__(self , customer , restaurant , rating ):
        self.customer = customer 
        self.restaurant = restaurant
        self.rating = rating 
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating
    
    @classmethod
    def all (cls):
        return cls.all_reviews
    
name = Review("Jane","All You Can Eat",8)

all_reviews = Review.all()

for review in all_reviews:
    print(f"Customer:{review.customer}, Restaurant:{review.restaurant} ,Rating:{review.rating}")
