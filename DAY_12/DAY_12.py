import csv

def create_csv_file(filename):
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
      
        writer.writerow(['name', 'age', 'city'])
        
        while True:
            
            name = input("Enter name (or type 'exit' to finish): ")
            if name.lower() == 'exit':
                break
            
            age = input("Enter age: ")
            city = input("Enter city: ")
            
            
            writer.writerow([name, age, city])
            print("Data added successfully.")


filename = 'data.csv'
create_csv_file(filename)

print(f"Data has been written to {filename}.")