class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []  # Initialize an empty list of reviews for this restaurant
        Restaurant.restaurants.append(self)

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews

    def customers(self):
        customer_set = set()
        for review in self.reviews:
            customer_set.add(review.customer())
        return list(customer_set)

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum(review.rating() for review in self.reviews)
        return total_rating / len(self.reviews)

    @classmethod
    def all(cls):
        return cls.restaurants

    def add_review(self, review):
        self.reviews.append(review)
