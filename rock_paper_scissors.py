import random

def get_winner(player, computer):
    if player == computer:
        return "tie"
    wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    return "player" if wins_against[player] == computer else "computer"

def display_choice(choice):
    art = {
        "rock":     "  _____\n |     |\n | ROCK|\n |_____|\n",
        "paper":    "  _____\n |     |\n |PAPER|\n |_____|\n",
        "scissors": "  _____\n |     |\n | SCI |\n |_____|\n",
    }
    return art[choice]

def main():
    choices = ["rock", "paper", "scissors"]
    scores = {"player": 0, "computer": 0, "ties": 0}

    print("=" * 45)
    print("       ROCK  ✊  PAPER  ✋  SCISSORS  ✌️")
    print("=" * 45)
    print("  Commands: rock | paper | scissors | quit\n")

    while True:
        player = input("Your choice: ").strip().lower()

        if player == "quit":
            print("\n--- Final Scores ---")
            print(f"  You     : {scores['player']}")
            print(f"  Computer: {scores['computer']}")
            print(f"  Ties    : {scores['ties']}")
            print("\nThanks for playing! Goodbye 👋")
            break

        if player not in choices:
            print("❌ Invalid choice! Enter rock, paper, scissors, or quit.\n")
            continue

        computer = random.choice(choices)

        print(f"\n  You       vs   Computer")
        print(f"  {player.upper():<10}  vs   {computer.upper()}")
        print()

        result = get_winner(player, computer)

        if result == "tie":
            scores["ties"] += 1
            print("  🤝 It's a TIE!\n")
        elif result == "player":
            scores["player"] += 1
            print(f"  🎉 You WIN! {player.capitalize()} beats {computer}.\n")
        else:
            scores["computer"] += 1
            print(f"  💻 Computer WINS! {computer.capitalize()} beats {player}.\n")

        print(f"  Score → You: {scores['player']}  |  Computer: {scores['computer']}  |  Ties: {scores['ties']}")
        print("-" * 45)

if __name__ == "__main__":
    main()
