# Program to demonstrate Game Character Design

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_details(self):
        print("Character Name:", self.name)
        print("Health:", self.health)


class Warrior(Character):
    def attack(self):
        print(self.name, "attacks with a sword!")


class Wizard(Character):
    def attack(self):
        print(self.name, "uses magic power!")


class Archer(Character):
    def attack(self):
        print(self.name, "shoots an arrow!")


# Create character objects
player1 = Warrior("Thor", 100)
player2 = Wizard("Harry", 80)
player3 = Archer("Robin", 90)

# Display character details
player1.show_details()
player1.attack()

print()

player2.show_details()
player2.attack()

print()

player3.show_details()
player3.attack()