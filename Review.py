class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating  # Rename the attribute to avoid conflicts
        Review.reviews.append(self)

    def rating(self):
        return self.rating_value

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    @classmethod
    def all(cls):
        return cls.reviews
