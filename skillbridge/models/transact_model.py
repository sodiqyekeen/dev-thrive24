class Transact:
    def __init__(self, id, payment_reference, payment_status):
        self.id = id
        self.payment_reference = payment_reference
        self.payment_status = payment_status
    
    def __dict__(self):
        return {
            'id': self.id,
            'status': self.payment_status
        }

    def get_id(self):
        return self.id

    def get_payment_reference(self):
        return self.payment_reference
    
    def get_payment_status(self):
        return self.payment_status
    
    