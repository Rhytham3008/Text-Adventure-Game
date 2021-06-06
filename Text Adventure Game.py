import time
import random

ans_A = ["A", "a"]
ans_B = ["B", "b"]
ans_C = ["C", "c"]
yes = ["Y", "y", "yes", "Yes", "yep","Yep"]
no = ["N", "n", "no", "No", "Nope", "nope"]

sword = 0
flower = 0
speed_of_orc = [10,20,30,40]
your_speed = [10,30,45,50, 60]

required = ("\n Use only A, B or C\n")

def intro():
    print("After a drunken night out with freinds, you awaken the next morning in a thick forest. Head spinning and fighting the urge to vomit, you stand and marvel at the new unfamiliar setting. The peace quickly fades when you hear a grotesque sound emmiting behind you. A slobbering orc is running towards you")
    time.sleep(1)
    print("A. Grab the nearby rock and throw it at the orc \nB. Lie down and wait to be mauled\nC. Run")
    choice = input(">>>>>>")
    if choice in ans_A:
        option_rock()
    elif choice in ans_B:
        print("\nOh no! That was quick.\n You are no more")
    elif choice in ans_C:
        option_before_run()
    else:
        print(required)
        intro()

def option_rock():
    print("\nThe orc is stunned, but regains control. He begins running towards you again. Will you: ")
    time.sleep(1)
    print("\nA.Run \nB Throw another rock. \nC Run towards a nearby cave")
    choice = input(">>>>")
    if choice in ans_A:
        option_mid_run()
    elif choice in ans_B:
        print("\n You decided to throw another rock at the orc. Unfortunately the second rock didn't hit the orc. The Orc attack you and you are done")
        quit()
    elif choice in ans_C:
        option_cave()
    else:
        print(required)
        option_rock()

def option_cave():
    print("\n You were hesitent, since the cave was dark and omnious. Before you enter you notice a shiny sword. Will you pick it up? Y/N")
    choice = input(">>>>>")
    if choice in yes:
        sword = 1
    else:
        sword = 0
    print("\n What do you do next")
    time.sleep(1)
    print("A. Hide in silence \nB. Fight \nC. Run")
    choice = input(">>>")
    if choice in ans_A:
        print("\n You are now hidden while the orc tries to find you. Hide Safely!")
    elif choice in ans_B:
        if sword > 0:
            print("\nYou seem brave to take this chance. You are now trying to fight the orc. After a feirce battle you killed the beast and you have survived, and you returned your home safely YAY!!!!!!.")
        else:
            print("You tried to fight the beast without sword, you are now dead. ")
    elif choice in ans_C:
        print("You are now trying to run away from the orc. The question is: How fast can you run?")
        option_run()
    else:
        print(required)
        option_cave()

def option_run():
    print("You ran towards the outside of cave quietly, but the orc noticed you  ")
    random.choice(speed_of_orc)
    random.choice(your_speed)
    if your_speed < speed_of_orc:
        print("You tried to run fast but Orc ran faster than you and attacked you and then you died. RIP")
    elif speed_of_orc < your_speed:
        print("You tried to run fast and you were fast than the orc and you saw  a hunter in between and you asked him for help while you are running then the hunter shooted many arrow towards the orc and the orc was badly injured and the orc died finally and you survived. You thanked the hunter  and as you were lost you asked the hunter the route to city he told it to you and you came home safely. ")
    else:
        print(required)
        option_run()

def option_before_run():
    (random.choice(your_speed))
    (random.choice(speed_of_orc))
    if your_speed < speed_of_orc:
        print("You tried to run fast but Orc ran faster than you and attacked you and then you died. RIP")
    elif speed_of_orc < your_speed:
        print("You ran and ran in this hustle and bustle you got deeper into the forest and it was also the place where orcs lived. You should have been  surrounded by many orcs, but you ran very fast so they didn't know that a human was near them and then at last you saw the hunter and you asked him for help while you were running, then the hunter shooted many arrow towards the orc and the orc was badly injured then the orc finally died and you survived. You thanked the hunter  and as you were lost you asked the hunter the route to city he told it to you and you came to your home safely. ")
    else:
        print(required)
        option_before_run()

def option_mid_run():
    random.choice(your_speed)
    random.choice(speed_of_orc)
    if your_speed < speed_of_orc:
        print("You tried to run fast but Orc ran faster than you and attacked you and then you died. RIP")
    elif speed_of_orc < your_speed:
        print("You ran vary fast than orc but a small rock came in your way and you fell on the rock, you became unconscious and the orc came and threw you on the rock very badly and then you died ")
    else:
        print(required)
        option_mid_run()

intro()
