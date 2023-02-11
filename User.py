#!/usr/bin/env python
# coding: utf-8

# In[10]:


import json
class User():
    def __init__(self):
        self.order_history = {}
        self.l = []
    def name_registration(self):
        self.full_name = input("Enter Full Name:")
        self.number = int(input("Enter Contact Number:"))
        self.password = input("Enter new Password:")
        self.email = input("Enter your Email:")
        self.address = input("Enter your Address:")
        self.st = {"Full Name":self.full_name,"Mobile Number":self.number,"Password":self.password,"Email":self.email,"Address":self.address}
        with open("Full_details.json","w") as f: 
            json.dump(self.st,f)
        print("\nRegisterd user list\n")
        return self.st
    def login(self):
        with open("Full_details.json","r") as f:
            self.temp = json.load(f)
        self.mail = input("Enter Registered Email:")
        self.passs = input("Enter your Password:")
        
        if self.mail != self.temp["Email"]:
            print("Invalid Login ID ")
        else:
            if self.passs != self.temp["Password"]:
                print("Please Enter a Correct Password")
            else:
                print("\nLogin Successfully")
                return ""
    def options(self):
        print("1. Place New Order")
        print("2. Order History")
        print("3. Update Profile")
        self.ask = int(input("\nEnter the Id of the option that you want to choose:\n"))
        if self.ask == 1:
            print("\n")
            with open("Food_menu.json","r") as f: 
                dis=json.load(f)
                print(dis)
            placed = eval(input("\nEnter the Food Id that you want to order:\n"))
            placed_list = list(placed)
            
            for placed in placed_list:
                if placed == 1:
                    print("'Food Name': 'Tandoori Chicken ', 'Quantity': '4 pieces', 'Price': 'INR 240'")
                if placed ==2:
                    print("'Food Name': ' Vegan Burger ', 'Quantity': '1 Piece', 'Price': 'INR 320'")
                if placed ==3:
                    print("'Food Name': 'Truffle Cake ', 'Quantity': '500gm', 'Price': 'INR 900'")
            return placed_list
                    
                
        elif self.ask == 2:
            print("'Food Name': 'Tandoori Chicken ', 'Quantity': '4 pieces', 'Price': 'INR 240'")
            print("'Food Name': ' Vegan Burger ', 'Quantity': '1 Piece', 'Price': 'INR 320'")
            return ""
            
        elif self.ask == 3:
            self.y = input("\nPlease enter that you want to update in your Profile:")
            while self.y in self.st:
                if self.y == "Full Name":
                    self.st["Full Name"] = input("Enter Full Name:")
                elif self.y =="Mobile Number":
                    self.st["Mobile Number"] = int(input("Mobile Number:"))
                elif self.y =="Password":
                    self.st["Password"] = int(input("Enter Password:"))
                elif self.y =="Email":
                    self.st["Email"] = int(input("Enter Email:"))
                elif self.y =="Address":
                    self.st["Address"] = int(input("Enter Address:"))
                with open("Full_details.json","w") as f: 
                    json.dump(self.st,f)
                print("\nRegisterd user list\n")
                return self.st
    
    
new = User()
print(new.name_registration())
print("\nSuccessfully Registered\n")
print(new.login())
print(new.options())

