
# Online Python - IDE, Editor, Compiler, Interpreter
import secrets

def rock_paper_scissors():
    opponent_choices = ["rock", "paper", "scissors"]
    print("Let's play Rock, Paper, Scissors!")
    while True:
        selection = input("Choose rock, paper, scissors, or quit")
        opponent_selection = secrets.choice(opponent_choices)
        if selection != "rock" and selection != "paper" and selection != "scissors" and selection != "quit":
            result = "invalid"
        elif selection == "quit":
            break
        elif selection == "rock":
            if opponent_selection == "rock":
                result = "tie"
            elif opponent_selection == "paper":
                result = "lose"
            else:
                result = "win"
        elif selection == "paper":
            if opponent_selection == "rock":
                result = "lose"
            elif opponent_selection == "paper":
                result = "tie"
            else:
                result = "win"
        elif selection == "scissors":
            if opponent_selection == "rock":
                result = "lose"
            elif opponent_selection == "paper":
                result = "win"
            else:
                result = "tie"

            
        print("Computer chooses " + opponent_selection)        
        if result == "tie":
            print("That was a tie! Let's play again!")
        elif result == "win":
            print("You beat me! Let's play again!")
        elif result == "lose":
            print("You lose! Let's play again!")
        elif result == "invalid":
            print("Invalid selection.")
rock_paper_scissors()