import random as random

class player():
    def __init__(self, life_points, hunger):
        self.life_points = life_points
        self.hunger = hunger


class animal():
    def __init__(self, name, health, type):
        self.name = name
        self.health = health
        self.type = type

    def __str__(self):
        self.name = input("Enter his/her name:")
        self.health = 100
        return print(f'Status of {self.type}\nName:{self.name}\nHealth:{self.health}')



def welcome_(answer):
    print("Welcome to Old West champ")
    name = input("Please enter your Name:")
    print(f'Hello {name} are you ready to begin your journey in the west? y/n')
    answer = input()
    return answer


def get_answer():
    answer_direction = str(input("Where do you want to go,write down N/S/E/W\n"))
    print(f'Going {answer_direction}...')


answer = ""

if welcome_(answer) == "y":
    print("The journey begins")
    player_one = player(100, 100)
    get_answer()
    rand_number = random.randint(0,7)
    match rand_number:
        case 1:
            print("you found a dog")
            answer = input("Do you want to accept the dog y/n")
            if answer == "y":
                print("Chose a name for your dog")
                name=input("Enter the name of the dog")
        case 2:
            print("You found a cat")
        case 3:
            print("You found a forrest")
        case 4:
            print("you found some food")
        case 5:
            print("you found a house")
        case 6:
            print("you found a haunted house")


else:
    print("")
