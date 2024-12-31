#Change the vahed
def length(value, from_, to_):
    conversions = {
        'm': 1.0,
        'cm': 100.0,
        'km': 0.001,
        'in': 39.3701
    }
    return value * conversions[to_] / conversions[from_]

def convert_weight(value, from_, to_):
    conversions = {
        'kg': 1.0,
        'lb': 2.20462,
        'oz': 35.274
    }
    return value * conversions[to_] / conversions[from_]

def convert_temperature(value, from_, to_):
    if from_ == 'C' and to_ == 'F':
        return (value * 9/5) + 32
    elif from_ == 'F' and to_ == 'C':
        return (value - 32) * 5/9
    else:
        return value


print("Welcome to the Unit Converter")
print("Select conversion type: ")
print("1. Length")
print("2. Weight")
print("3. Temperature")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    value = float(input("Enter value: "))
    from_ = input("Enter from unit (m/cm/km/in): ")
    to_ = input("Enter to unit (m/cm/km/in): ")
    result = length(value, from_, to_)
    print(f"{value} {from_} is {result} {to_}")

elif choice == '2':
    value = float(input("Enter value: "))
    from_ = input("Enter from unit (kg/lb/oz): ")
    to_ = input("Enter to unit (kg/lb/oz): ")
    result = convert_weight(value, from_, to_)
    print(f"{value} {from_} is {result} {to_}")

elif choice == '3':
    value = float(input("Enter value: "))
    from_ = input("Enter from unit (C/F): ")
    to_ = input("Enter to unit (C/F): ")
    result = convert_temperature(value, from_, to_)
    print(f"{value} {from_} is {result}°{to_}")
else:
    print("Invalid choice.")