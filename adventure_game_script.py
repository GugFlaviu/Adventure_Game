import random as random
import time


class Item:
    def __init__(self, name, durabillity, found):
        self.name = name
        self.durabillity = durabillity
        self.found = found

    def __str__(self):
        return f'Status of {self.name}\nDurabillity:{str(self.durabillity)}\nFound:{str(self.found)} '


class Player:
    def __init__(self, name, life_points, hunger):
        self.name = name
        self.life_points = life_points
        self.hunger = hunger

    def __str__(self):
        return f'Status:{self.name}\nHealth:{str(self.life_points)}\n'


class Animal:
    def __init__(self, name, health, type):
        self.name = name
        self.health = health
        self.type = type

    def __str__(self):
        self.name = input("Enter his/her name:")

        self.health = 100
        return f'Status of {str(self.type)}\nName:{str(self.name)}\nHealth:{str(self.health)}'


def welcome_(answer):
    title = """
____________________________________________
   ____  _     _   __          __       _   
  / __ \| |   | |  \ \        / /      | |  
 | |  | | | __| |   \ \  /\  / /__  ___| |_ 
 | |  | | |/ _` |    \ \/  \/ / _ \/ __| __|
 | |__| | | (_| |     \  /\  /  __/\__ \ |_ 
  \____/|_|\__,_|      \/  \/ \___||___/\__|
  
___________________________________________"""
    print(f"{title}\nWelcome to Old West\nWhen you want to exit type EXIT")
    global name
    name = input("Please enter your Name:")
    print(f'Hello {name} are you ready to begin your journey in the west? Y/N:')
    while answer != "y":
        answer = input().lower()
        if answer == "y":
            return answer.lower()
        else:
            print("Please enter a valid answer")


def get_answer():
    while answer != "EXIT" or answer_direction != "n" or answer_direction != "s" or answer_direction != "e" or answer_direction != "w":
        answer_direction = str(input("Where do you want to go,write down N/S/E/W\n")).lower()
        if answer_direction == "n" or answer_direction == "s" or answer_direction == "e" or answer_direction == "w":
            print(f'Going {answer_direction.upper()}', end="")
            for i in range(1, 4):
                print(".", end="")
                time.sleep(1)
            break

        else:
            print("chose a VALID option")


def died():
    print("""
________________________________________

__     __           _____  _          _ 
\ \   / /          |  __ \(_)        | |
 \ \_/ /__  _   _  | |  | |_  ___  __| |
  \   / _ \| | | | | |  | | |/ _ \/ _` |
   | | (_) | |_| | | |__| | |  __/ (_| |
   |_|\___/ \__,_| |_____/|_|\___|\__,_|
   
________________________________________                                         
                                         
""")


answer = ""
if welcome_(answer) == "y":
    print("The journey begins")
    player_one = Player(name, 100, 100)
    monster = Player("monster", 100, 1)
    sword = Item("Sword", 100, False)
    get_answer()
    rand_number = random.randint(1, 7)
    while answer != "EXIT" or player_one.life_points <= 0:
        match rand_number:
            case 1:
                print("you found a dog")
                answer = input("Do you want to accept the dog Y/N\n")
                if answer == "y":

                    dog = Animal("dog", 100, "dog")
                    print(dog)
                    get_answer()
                    rand_number = random.randint(1, 7)
                else:
                    print(f"You left the {dog.type} and he is sad")
                    get_answer()
                    rand_number = random.randint(1, 7)
            case 2:
                print("You found a cat")
                answer = input("Do you want to accept the cat y/n")
                if answer == "y":

                    cat = Animal(" ", 100, "cat")
                    print(cat)
                    get_answer()
                    rand_number = random.randint(1, 7)
                else:
                    print(f"You left the {cat.type} and he is sad")
                    get_answer()
            case 3:
                print("You found a forrest")
                answer = input("Do you want to enter the forest? Y/N\n")
                answer.lower()

                if answer == "y":
                    print("You enter the forest", end="")
                    for i in range(1, 4):  # ads a little life to the game
                        print(".", end="")
                        time.sleep(1)

                    answer = input("You found a monster,do you want to attack him,Y/N\n").lower()
                    if answer == "y":
                        while monster.life_points >= 0 or player_one.life_points >= 0:
                            if sword.found:
                                monster.life_points -= 100
                                sword.durabillity -= 50
                                print(monster)
                                print("you killed the monster")
                                print(player_one, "\n", sword)
                                if monster.life_points <= 0 or player_one.life_points <= 0:
                                    break
                            else:
                                rand_hit = random.randint(1, 3)
                                monster.life_points -= rand_hit * 10
                                rand_hit = random.randint(1, 3)
                                player_one.life_points -= rand_hit * 10


                                print("Attaking the monster", end="")
                                for i in range(3):
                                    print(".", end="")
                                    time.sleep(1)
                                print(monster, "\n", player_one)
                                if monster.life_points <= 0 or player_one.life_points <= 0:
                                    break
                        if player_one.life_points <= 0:
                            died()
                            break

                        else:
                            get_answer()
                            rand_number = random.randint(1,7)
                    elif answer == "n":
                        rand_hit = random.randint(1, 3)
                        rand_choice = random.randint(1, 2)
                        if rand_choice == 1:
                            print("The monster hit you\n")
                            player_one.life_points -= 5
                            print(player_one)
                            answer = input("Do you want to hit the monster back Y/N\n").lower()
                            if answer == "y":


                                rand_hit = random.randint(1, 3)
                                while monster.life_points >= 0 or player_one.life_points >= 0:
                                    if sword.found:
                                        print("Attaking the monster", end="")
                                        for i in range(3):
                                            print(".", end="")
                                            time.sleep(1)
                                        monster.life_points -= 100
                                        sword.durabillity -= 50
                                        print(monster)
                                        print("you killed the monster")
                                        print(player_one, "\n", sword)
                                        if monster.life_points <= 0 or player_one.life_points <= 0:
                                            break
                                    else:

                                        monster.life_points -= rand_hit * 10
                                        player_one.life_points -= rand_hit * 10
                                        rand_hit = random.randint(1, 2)
                                        print(monster, "\n", player_one)
                                        print("Attaking the monster", end="")
                                        for i in range(3):
                                            print(".", end="")
                                            time.sleep(1)
                                get_answer()
                                rand_number = random.randint(1, 7)
                            else:
                                died()
                                break

                    else:
                        print("He did not saw you\n")
                        get_answer()
                        rand_number = random.randint(1, 7)

                else:
                    get_answer()
                    rand_number = random.randint(1, 7)

            case 4:
                print("you found some food")
                if player_one.life_points <= 100:
                    player_one = 100
                    print("Your life restored\n")
                    print(player_one)
                get_answer()
                rand_number = random.randint(1, 7)
            case 5:
                answer = input("You see a house do you enter?Y/N\n").lower()
                if answer == "y":
                    print("you found a sword")
                    sword.found = True
                    get_answer()
                    rand_number = random.randint(1, 7)
                else:
                    print("you walk away")
                    get_answer()
                    rand_number = random.randint(1, 7)

            case 6:
                print("you found an old house in the middle of texas")
                answer = input("Do you want to enter the house? Y/N\n").lower()
                if answer == "y":
                    print("A criminal shoot you in the head", end="")
                    for i in range(5): #it was better if this was a function because I used this line of code to many times
                        print(".", end="")
                        time.sleep(1)
                    died()
                else:
                    print("you walk away\n")

                    get_answer()
                    rand_number = random.randint(1, 7)

            case 7:
                print("you found a sword")
                sword.found = True


                get_answer()
                rand_number = random.randint(1, 7)

elif answer == "n":
    print("Exiting Now", end="")
    for i in range(3):
        print(".", end="")
        time.sleep(1)
