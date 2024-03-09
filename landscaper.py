def main():
    # Dictionary containing tools with their cost and income
    tools = {
        "teeth": {"cost": 0, "income": 1},
        "rusty scissors": {"cost": 5, "income": 5},
        "push lawnmower": {"cost": 25, "income": 50},
        "battery-powered lawnmower": {"cost": 250, "income": 100},
        "team of starving students": {"cost": 500, "income": 250}
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
            # Check if the tool is valid and player has enough money to buy it
            if new_tool in tools and money >= tools[new_tool]["cost"]:
                money -= tools[new_tool]["cost"]
                current_tool = new_tool
                print(f"\nYou have bought a {current_tool}.")
            else:
                print("\nInvalid input or not enough money to buy this tool.")
        elif choice == "3":
            print("\nExiting game...")
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()