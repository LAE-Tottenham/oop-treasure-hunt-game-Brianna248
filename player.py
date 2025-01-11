import questionary
class Player():
    def __init__(self, given_name, item_being_held):
        self.location = "Street"
        self.given_name = given_name
        self.no_of_inventory_items = int(3)
        self.max_inventory = int(5)
        self.items = ["phone", "Hair Pin"]
        self.item_being_held = item_being_held
        self.inventory = [] #cant have more than 2 items in backpack at once

    def add_item_to_inventory (self, inventory, item_being_held):
        size = len(inventory)
        if size == "2":
            print("You cannot put an item into your backpack as it is full.")
            print(" ")
            answer = questionary.select("Would you like to remove an item in your inventory?", 
                    choices=[
                        "Yes",
                        "No",
                    ]).ask()
            if answer == "Yes":
                answer = questionary.select("Which item would you like to remove?",
                            choices=[
                                self.inventory[0],
                                self.inventory[1],
                            ]).ask()
                if answer == self.invenotory[1]:
                    self.inventory.remove(0)
                    return(self.inventory[0] + " has been taken out of your backpack.")
                else:
                    self.inventory.remove(1)
                    return(self.inventory[1] + " has been taken out of your backpack.")
            else: 
                return ("Okay. You have just placed "+ item_being_held + " back down.")
        else: 
            self.inventory.append(item_being_held)
            return("Item successfully placed in backpack")
        

    def calculate_total_inventory_size (self, no_of_inventory_items, max_inventory, inventory ):
        inventory_size = (max_inventory - no_of_inventory_items)
        inventory_size = (inventory_size - self.size)
        return ("You can store " + inventory_size +" more items in your backpack.")

    def use_item (self):
        answer = questionary.select("What item would you like to use?", 
                    choices=[
                        self.items[0],
                        self.items[1],
                        self.items[2],
                        self.inventory[0], 
                        self.inventory1[1],
                    ]).ask()
        if answer ==  and self.location == :