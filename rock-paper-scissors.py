import random

# Avalible game choices   
GAME_CHOICES = ["rock", "paper", "scissor"]

# Winning combination
WIN_RULES = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def rock_paper_scissors():

    # Enter player name
    while True:
        name = input("Enter your name: ").strip()

        if name:
            print("\n---- Rules ----")
            print(
                f"Hi {name}! Players chant 'Rock, Paper, Scissors, Shoot!'\n"
                "and simultaneously form one of three hand shapes.\n"
                "Winners are decided instantly:\n"
                "- Rock crushes Scissors\n"
                "- Scissors cuts Paper\n" 
                "- Paper covers Rock\n" 
                "Ties result in a rematch."
            )
            print("_" * 70)
            break
        
        print("Please enter a valid name!")
    
    # Start the game
    start = input(f"\n{name}, are you ready to start? (yes/no): ").strip().lower()
    
    if start != 'yes':
        print('Bye!')
        return
    
    # Main game loop
    while True:
        user = input("Choose (rock/paper/scissor) or type 'quit' to exit: ").strip().lower()

        # Exit game
        if user == 'quit':
            print(f"Thanks for plaing, {name}! Bye!")
            break
        
        # Validate input
        if user not in GAME_CHOICES:
            print("Invalid choise! Please choose rock, paper, or scissors.")
            continue
            
        # Random bot choise
        bot = random.choice(GAME_CHOICES)
        
        print(f"\n{name}: {user.capitalize()} vs Bot: {bot.capitalize()}")

        # Check game result
        if user == bot:
            print("Draw!\n")
        
        elif WIN_RULES[user] == bot:
            print("You Win!\n")
        
        else:
            print("You Lose\n")

# Start the game
rock_paper_scissors()
    