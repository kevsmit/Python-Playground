import random

CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def winner(player, computer):
    if player == computer:
        return "tie"
    return "player" if BEATS[player] == computer else "computer"


def main():
    wins = losses = ties = 0
    print("Rock Paper Scissors! Type rock, paper, scissors or q to quit.")
    while True:
        player = input("Your move: ").strip().lower()
        if player == "q":
            break
        if player not in CHOICES:
            print("Please type rock, paper or scissors.")
            continue
        computer = random.choice(CHOICES)
        result = winner(player, computer)
        print(f"Computer chose {computer}.")
        if result == "player":
            wins += 1
            print("You win!")
        elif result == "computer":
            losses += 1
            print("You lose.")
        else:
            ties += 1
            print("It's a tie.")
    print(f"Final score - wins: {wins}, losses: {losses}, ties: {ties}")


if __name__ == "__main__":
    main()
