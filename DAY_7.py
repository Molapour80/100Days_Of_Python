import random

first_names_male = [
    "Ali", "Reza", "Mohammad", "Omid", "Farid",
    "Saeed", "Navid", "Kaveh", "Arash", "Amir"
]

first_names_female = [
    "Fatemeh", "Zahra", "Sara", "Niloofar", "Leila",
    "Parisa", "Shirin", "Nazanin", "Mina", "Yasaman"
]

last_names = [
    "Ahmadzadeh", "Mohammadi", "Karimi", "Javan", "Sadeghi",
    "Hosseini", "Rezaei", "Gholami", "Khodadadi", "Fakhradi"
]

def generate_random_name(gender, num_names):
   
    names = []
    for _ in range(num_names):
        if gender == 'male':
            first_name = random.choice(first_names_male)
        elif gender == 'female':
            first_name = random.choice(first_names_female)
        else:
            raise ValueError("Gender must be 'male' or 'female'.")

        last_name = random.choice(last_names)
        names.append(f"{first_name} {last_name}")

    return names  

def main():
    gender = input("Choose gender ('male' or 'female'): ").strip().lower()
    num_names = int(input("How many random names would you like to generate? "))

    random_names = generate_random_name(gender, num_names)
    
    print(f"\nRandom {gender} names:")
    for name in random_names:
        print(name)

if __name__ == "__main__":
    main()