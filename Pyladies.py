


print("Welcome to the dungeon!")
name = input("May I kindly ask your name?")
print(f"Ok {name}, heres the deal: You need to make a choice between door number 1 and door number 2, which one do you choose?")
door = input("So? Make a choice! We dont have all day")
if door == "1":
    print(f"Great, you get to continue your adventure {name}")
else:
    print("Oh, you are dead, sorry :-(...")
    exit(0)


print("Ok, it gets more complicated at this point, no more of the choosing door crap")
couldron = input("Now you have the choice to drink either from the black, green or red cauldron, what do you want to do? Choose wisely!")

if couldron.lower() == "green":
    print(f"Congratulations, you are lucky to be alive {name}")
elif couldron.lower() == "red":
    print("Who chooses to drink from a red couldron? You are dead of course...")
else:
    print("Oh, you are dead, sorry :-(...")

