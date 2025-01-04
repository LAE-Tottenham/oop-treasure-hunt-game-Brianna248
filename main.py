#from place import Place
#from item import Item
#from player import Player

#class Game():
#    def __init__(self):
        #self.current_place = None
    
        # add more atributes as needed

    #def setup(self):
        # here you will setup your Game
        # places
        
        #front_of_house = Place('Front of House', 10)
        #sidewalk = Place('Sidewalk', 5)
        #entrance_corridor = Place('Entrance Corridor', 4, True) # entrance corridor is locked
        #garden = Place('Garden', 15)
        #shed = Place('Shed', 3)
        #livingroom = Place('Livingroom', 50)
        
        #home.add_next_place(front_of_house)
        #home.add_next_place(sidewalk)
        #home.add_next_place(entrance_corridor)
        #garden.add_next_place(shed)
        # etc. 
        
        # items
        #hammer = Item('Hammer')
        #pen = Item('Pen')

        #home.add_item(hammer)
        #bedroom.add_item(pen)

        # home will be our starting place
        #elf.current_place = home
        
        # finish the setup function...

    #def start(self):
        #print("Welcome to my game...")
        #print("Storyline...")
        #name = input("Enter player name: ")
        #player = Player(name)

        #print("You are currently in " + self.current_place.name)
        #self.current_place.show_next_places()
        #opt = input("""
#What would you like to do?
#1. Go to a place
#2. Pickup item
#3. Check inventory
#etc.      
#""")
#        if opt == "1":
#            # add code
#            pass
#        elif opt == "2":
#            # add code
#            pass
#        elif opt == "3":
#            # add code
#           pass
            


import questionary
print(" ")
print("Welcome to my game!")
print(" ")
print("In this game, your bestfriend has been kidnapped. You were on the phone to her while she was walking home and she screamed and abruptly hung up. You called her back a couple times only to be met with the irritating sound of her automated voicemail. You checked her location and saw that her phone is in a neighbourhood 40 minutes from her house and 20 from yours. You instinctively grab your backpack and your keys and sprint out the door towards where you last heard from her.")
print(" ")
print("You reach her location- a neighbourhood with rows and rows of seemingly identical houses- with nobody in sight other than an old man walking down the sidewalk in your direction. You quicky look around trying to find any clues as to where she might be and decide to call her phone one more time. You see something in a bush beside the sidewalk on the other side of the road light up. Her phone.")
print(" ")
print("Just as you put your phone down and start heading towards her phone in hopes you'll find any other clues that might lead you to her the old man approaches you. He looks frail and old and is struggling to walk, resting on his wobbling cane."+" 'Please help me cross the road young lady. My home is just on the other side of the road, right there. I made it this far but I doubt I can make it much further. Please help me get home'.")
print(" ")
print("You hesitate for a moment. His house was only two houses down from your friend's phone but you aren't sure if you've got much time to spare. Your bestfriend could be anywhere and its nearing 6pm meaning you'll only have an hour before it starts getting dark.")
print(" ")
questionary.select("What would you like to do?", 
                   choices=[
                       "Help the old man get to his house",
                       "Cross the road and take your friend's phone",
                   ]).ask()

