class TreasureIslandGame:
    def __init__(self):
        print("Welcome to Treasure Island! Your mission is to find the treasure.")

    def start_game(self):
        choice = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()
        if choice == "left":
            self.lake_scenario()
        else:
            print("You fell into a hole. Game Over.")

    def lake_scenario(self):
        choice = input(
            "You have come to a lake. There is an island in the middle of the lake.\n"
            "Type 'wait' to wait for a boat or 'swim' to swim across: "
        ).lower()
        if choice == "wait":
            self.door_scenario()
        else:
            print("You were attacked by trout. Game Over.")

    def door_scenario(self):
        choice = input(
            "You arrived at the island unharmed. There is a house with three doors: red, yellow, and blue.\n"
            "Which color do you choose? "
        ).lower()
        if choice == "red":
            print("You were burned by fire. Game Over.")
        elif choice == "blue":
            print("You were eaten by beasts. Game Over.")
        elif choice == "yellow":
            print("Congratulations! You found the treasure. You Win!")
        else:
            print("Invalid choice. Game Over.")

if __name__ == "__main__":
    game = TreasureIslandGame()
    game.start_game()
