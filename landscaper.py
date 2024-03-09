def main():
    # Dictionary containing tools with their cost and income
    tools = {
        "teeth": {"cost": 0, "income": 1},
        "rusty scissors": {"cost": 5, "income": 5},
        "push lawnmower": {"cost": 25, "income": 50},
        "battery-powered lawnmower": {"cost": 250, "income": 100},
    }

    # Initial money, current tool, and win amount
    money = 0
    current_tool = "teeth"
    win_amount = 1000
    
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
        print("2. Buy new tool")
        print("3. Exit game")

        # Get player's choice
        choice = input("\nEnter your choice: ")

        # Perform actions based on player's choice
        if choice == "1":
            money += tools[current_tool]["income"]
        elif choice == "2":
            # Display available tools to buy
            print("\nAvailable tools to buy:")
            for tool, info in tools.items():
                if money >= info["cost"]:
                    print(f"{tool.capitalize()} - Cost: ${info['cost']} - Income: ${info['income']} per day")

            # Get the tool player wants to buy
            new_tool = input("\nEnter the tool you want to buy: ").lower()