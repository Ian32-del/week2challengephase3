class Review :
    all_reviews = []
    def __init__(self , customer , restuarant , rating ):
        self.customer = customer 
        self.restuarant = restuarant
        self.rating = rating 
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating
    
    