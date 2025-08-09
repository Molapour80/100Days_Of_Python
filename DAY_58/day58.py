##..........H............
import random

def coin_flip():
    """Simulate a coin flip (heads or tails)"""
    result = random.choice(['Heads', 'Tails'])
    return result

def dice_roll(sides=6):
    """Simulate a dice roll with specified number of sides"""
    if sides < 2:
        return "Dice must have at least 2 sides"
    result = random.randint(1, sides)
    return result

def simulator():
    """Main simulator function with menu interface"""
    print("Coin and Dice Simulator")
    print("1. Flip a coin 🪙 ")
    print("2. Roll a 6-sided dice 🎲")
    print("3. Roll a custom-sided dice ")
    print("4. Exi ⚠️")
    
    while True:
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print(f"Coin flip result: {coin_flip()}")
        elif choice == '2':
            print(f"Dice roll result: {dice_roll()}")
        elif choice == '3':
            try:
                sides = int(input("Enter number of dice sides: "))
                if sides < 2:
                    print("Dice must have at least 2 sides")
                else:
                    print(f"Dice roll result: {dice_roll(sides)}")
            except ValueError:
                print("Please enter a valid number :))))")
        elif choice == '4':
            print("Thank you for using the simulator. Goodbye!👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4.-.")

if __name__ == "__main__":
    simulator()