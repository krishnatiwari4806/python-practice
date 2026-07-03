class customer :

    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.city,self.address.pin, self.address.country)

    def edit_profile(self,new_name,new_gender,new_address):
        self.name = new_name
        self.address.edit_address(new_address.city,new_address.pin,new_address.country)    
    
class address :

    def __init__(self,city,pin,country):
        self.city = city
        self.pin = pin
        self.country = country

    
    def edit_address(self,new_city,new_pin,new_country):
        self.city = new_city
        self.pin = new_pin
        self.country = new_country

add1 =address("New York", 10001, "USA")
cust1 = customer("krishna", "Male", add1)



cust1.print_address()
cust1.edit_profile("Ramesh", "Male", address("Los Angeles", 90001, "USA"))
cust1.print_address()