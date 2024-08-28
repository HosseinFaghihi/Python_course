import random

class RPSGame:
    def __init__(self):
        self.items = {1: "Rock", 2: "Paper", 3: "scissors"}

    def get_user_choice(self):
        """
        Gets the user's choice for Rock-Paper-Scissors.

        Returns: the user's choice as an intiger
        Raises: ValueError if the user enters a non-integer value

        """
        while True:
            try:
                user_choice = int(input("Enter your choice as a number:\n1) Rock,\n2) Paper,\n3) Scissors\n"))
                if user_choice in range(1, 4):
                    return user_choice
                else:
                    print("Please enter a number between 1 and 3.")
            except ValueError:
                print("Please enter a number.")

    def get_computer_choice(self):
        """
        Generates a random choice for the computer.

        Returns: the computer's choice as an intiger
        """
        computer_choice = random.randint(1, 3)
        print("Computer chose:", self.items[computer_choice])
        return computer_choice

    def determine_winner(self, user_choice, computer_choice):
        """
        Determines the winner of the game.

        Args:
            user_choice (int): the user's choice
            computer_choice (int): the computer's choice

            Returns: the winner of the game as a string
        """
        if user_choice == computer_choice:
            return "Tie!"
        elif user_choice == 1:
            if computer_choice == 2:
                return "You lost!"
            else:
                return "You won!"
        elif user_choice == 2:
            if computer_choice == 1:
                return "You won!"
            else:
                return "You lost!"
        elif user_choice == 3:
            if computer_choice == 1:
                return "You lost!"
            else:
                return "You won!"

    def play_game(self, final_score):
        """
        Plays the Rock-Paper-Scissors game until the final score is reached.

        Args:
            final_score (int): the final score for the game

            Returns: None
        """
        user_score = 0
        computer_score = 0

        while user_score < final_score and computer_score < final_score:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            result = self.determine_winner(user_choice, computer_choice)

            if result == "You won!":
                user_score += 1
            elif result == "You lost!":
                computer_score += 1

            print(f"Player: {user_score}, \nComputer: {computer_score}")
            print(result)

        if user_score == final_score:
            print("Congratulations! You won.")
        else:
            print("Better luck next time.")

if __name__ == "__main__":
    print("Welcome to the Rock-Paper-Scissors game!")
    input("Enter your name:\n")
    final_score = int(input("How many points do you want to play to?\n"))

    game = RPSGame()
    game.play_game(final_score)

    print("Thank you for playing!")
