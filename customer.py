class Customer :

    all_customers = []
    def __init__(self , given_name , family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self) 

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
    
customer1 = Customer("George", "Washington")

all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name())