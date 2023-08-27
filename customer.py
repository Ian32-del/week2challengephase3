class Customer :
    def __init__(self , given_name , family_name):
        self.given_name = given_name
        self.family_name = family_name

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
    

    def all(cls):

        return all_customer
    
customer1 = Customer("George", "Washington")

all_customer = Customer.all()
for customer in all_customer:
    print(customer.full_name())