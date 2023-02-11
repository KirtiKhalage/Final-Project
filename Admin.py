#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
class Admin():
    def __init__(self):
        self.food_item_list = {}
        self.food_id = len(self.food_item_list)+1
    def add_food_item(self):
        self.food_name = input("Enter Food name:")
        self.quantity = input("Enter Quantity:")
        self.price = input("Enter Price:")
        self.discount = int(input("Enter discount:"))
        self.stock = int(input("Enter Stock:"))
        self.food_item = {"Food Name":self.food_name,"Quantity":self.quantity,"Price":self.price,"Discount":self.discount,"Stock":self.stock}
        self.food_id = len(self.food_item_list)+1
        self.food_item_list[self.food_id] = self.food_item
        with open("Food_menu.json","w") as f: 
            json.dump(self.food_item_list,f)
        print("\nAdded Food item list\n")
        return self.food_item_list
    def edit_food_item(self):
        food_item_id = int(input("\nEnter Food ID that you want to edit:"))
        while food_item_id in range(1,len(self.food_item_list)+1):
            y = input("\nWhat you need to edit?:")
            if y == "Food Name":
                self.food_item_list[food_item_id]["Food Name"] = input("Enter Food name:")
            elif y =="Quantity":
                self.food_item_list[food_item_id]["Quantity"] = int(input("Enter Quantity:"))
            elif y =="Price":
                self.food_item_list[food_item_id]["Price"] = int(input("Enter Price:"))
            elif y =="Discount":
                self.food_item_list[food_item_id]["Discount"] = int(input("Enter Discount:"))
            elif y =="Stock":
                self.food_item_list[food_item_id]["Stock"] = int(input("Enter Stock:"))
            with open("Food_menu.json","w") as f:
                json.dump(self.food_item_list,f)
            return ""
        return "Enter valid Food ID"
    def view_food_list(self):
        with open("Food_menu.json","r") as f: 
            y = json.load(f)
        print("Edited Food item list\n")
        return y
    def remove_food_item(self):
        food_id = int(input("Enter Food ID that you want to remove:"))
        del self.food_item_list[food_id]
        with open("Food_menu.json","w") as f: 
            json.dump(self.food_item_list,f)
        print("\nRemaining Food item list after deletion\n")
        return self.food_item_list
        
x = Admin()
print(x.add_food_item())
print(x.add_food_item())
print(x.add_food_item())
print(x.add_food_item())
print(x.edit_food_item())
print(x.view_food_list())
print(x.remove_food_item())

