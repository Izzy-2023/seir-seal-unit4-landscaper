def main():
    # Dictionary containing tools with their cost and income
    tools = {
        "teeth": {"cost": 0, "income": 1},
        "rusty scissors": {"cost": 5, "income": 5},
    }

    # Initial money, current tool, and win amount
    money = 0
    current_tool = "teeth"

    
    # Welcome message
    print("Welcome to the Landscaping Business Game!")

    # Main game loop
    while True:
        # Display current status
        print(f"\nYou currently have ${money}. Your current tool is: {current_tool}")

        # Check if player has enough money and current tool to win
        if money >= win_amount and current_tool == "team of starving students":
            print("\nCongratulations! You've won the game!")
            break

        # Display options
        print("\nOptions:")
        print("1. Work with current tool")


        # Get player's choice
        choice = input("\nEnter your choice: ")