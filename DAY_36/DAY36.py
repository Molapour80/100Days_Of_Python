def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Determine the category based on BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("BMI Calculator")
    
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    
    except ValueError:
        print("Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()