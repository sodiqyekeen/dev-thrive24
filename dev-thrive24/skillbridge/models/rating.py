class Rating:
    def __init__(self, id, tutor_id, user_id, rating, review):
        self.id = id
        self.tutor_id = tutor_id
        self.user_id = user_id
        self.rating = rating
        self.review = review

    def get_id(self):
        return self.id

    def get_tutor_id(self):
        return self.tutor_id
    
    def get_user_id(self):
        return self.user_id
    
    def get_rating(self):
        return self.rating

    def get_review(self):
        return self.review