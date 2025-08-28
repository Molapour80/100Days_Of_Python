class Employee:
    def __init__(self, name, base_salary, overtime_hours=0, overtime_rate=1.5):
        self.name = name
        self.base_salary = base_salary
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate
        
    def calculate_overtime_pay(self):
        """Calculate overtime pay"""
        hourly_rate = self.base_salary / 160  # Assume 160 working hours per month
        return self.overtime_hours * hourly_rate * self.overtime_rate
    
    def calculate_tax(self, gross_salary):
        """Calculate tax (simple example)"""
        if gross_salary <= 3000000:
            return 0
        elif gross_salary <= 5000000:
            return gross_salary * 0.1
        else:
            return gross_salary * 0.15
    
    def calculate_insurance(self, gross_salary):
        """Calculate insurance (simple example)"""
        return gross_salary * 0.07
    
    def calculate_net_salary(self):
        """Calculate net salary"""
        # Base salary + overtime
        gross_salary = self.base_salary + self.calculate_overtime_pay()
        
        # Deductions
        tax = self.calculate_tax(gross_salary)
        insurance = self.calculate_insurance(gross_salary)
        total_deductions = tax + insurance
        
        # Net salary
        net_salary = gross_salary - total_deductions
        
        return {
            'gross_salary': gross_salary,
            'tax': tax,
            'insurance': insurance,
            'total_deductions': total_deductions,
            'net_salary': net_salary
        }
    
    def print_payroll(self):
        """Print payroll slip"""
        result = self.calculate_net_salary()
        
        print("=" * 50)
        print(f"PAYROLL SLIP - {self.name}")
        print("=" * 50)
        print(f"Base Salary: {self.base_salary:,.0f} Toman")
        print(f"Overtime Hours: {self.overtime_hours} hours")
        print(f"Overtime Pay: {self.calculate_overtime_pay():,.0f} Toman")
        print(f"Gross Salary: {result['gross_salary']:,.0f} Toman")
        print("-" * 50)
        print(f"Tax: {result['tax']:,.0f} Toman")
        print(f"Insurance: {result['insurance']:,.0f} Toman")
        print(f"Total Deductions: {result['total_deductions']:,.0f} Toman")
        print("=" * 50)
        print(f"Net Salary: {result['net_salary']:,.0f} Toman")
        print("=" * 50)


def main():
    """Main program"""
    print("Payroll Calculation System")
    print("=" * 30)
    
    # Get user input
    name = input("Employee Name: ")
    base_salary = float(input("Base Salary (Toman): "))
    overtime_hours = float(input("Overtime Hours: "))
    
    # Create employee object
    employee = Employee(name, base_salary, overtime_hours)
    
    # Calculate and display payroll
    employee.print_payroll()
    
    # Option to save to file
    save_option = input("Do you want to save the payroll slip? (y/n): ")
    if save_option.lower() == 'y':
        with open(f"payroll_{name}.txt", "w", encoding="utf-8") as f:
            f.write(f"Payroll Slip - {name}\n")
            f.write(f"Base Salary: {base_salary:,.0f} Toman\n")
            f.write(f"Overtime Hours: {overtime_hours}\n")
            result = employee.calculate_net_salary()
            f.write(f"Net Salary: {result['net_salary']:,.0f} Toman\n")
        print("Payroll slip saved successfully.")


def batch_calculation():
    """Batch payroll calculation"""
    employees = []
    
    print("Batch Payroll Calculation")
    print("=" * 30)
    
    while True:
        name = input("Employee Name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        
        base_salary = float(input("Base Salary (Toman): "))
        overtime_hours = float(input("Overtime Hours: "))
        
        employee = Employee(name, base_salary, overtime_hours)
        employees.append(employee)
        print("-" * 30)
    
    # Display results
    print("\nBatch Calculation Results:")
    print("=" * 60)
    print(f"{'Name':<20} {'Gross Salary':<15} {'Net Salary':<15}")
    print("-" * 60)
    
    for emp in employees:
        result = emp.calculate_net_salary()
        print(f"{emp.name:<20} {result['gross_salary']:,.0f} Toman {result['net_salary']:,.0f} Toman")


def add_bonus_deductions():
    """Extended version with bonuses and additional deductions"""
    employees = []
    
    print("Advanced Payroll with Bonuses & Deductions")
    print("=" * 40)
    
    while True:
        name = input("Employee Name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        
        base_salary = float(input("Base Salary (Toman): "))
        overtime_hours = float(input("Overtime Hours: "))
        bonus = float(input("Bonus Amount (Toman): "))
        loan_deduction = float(input("Loan Deduction (Toman): "))
        
        # Create employee and add custom attributes
        employee = Employee(name, base_salary, overtime_hours)
        employee.bonus = bonus
        employee.loan_deduction = loan_deduction
        
        # Calculate extended payroll
        result = employee.calculate_net_salary()
        extended_net = result['net_salary'] + bonus - loan_deduction
        
        employees.append({
            'employee': employee,
            'bonus': bonus,
            'loan_deduction': loan_deduction,
            'extended_net': extended_net
        })
        print("-" * 40)
    
    # Display advanced results
    print("\nAdvanced Payroll Results:")
    print("=" * 80)
    print(f"{'Name':<15} {'Base':<10} {'Overtime':<10} {'Bonus':<10} {'Loans':<10} {'Net':<15}")
    print("-" * 80)
    
    for emp_data in employees:
        emp = emp_data['employee']
        result = emp.calculate_net_salary()
        print(f"{emp.name:<15} {emp.base_salary:,.0f} {emp.overtime_hours:<10} "
              f"{emp_data['bonus']:,.0f} {emp_data['loan_deduction']:,.0f} "
              f"{emp_data['extended_net']:,.0f}")


if __name__ == "__main__":
    while True:
        print("\nMain Menu:")
        print("1. Individual Payroll Calculation")
        print("2. Batch Payroll Calculation")
        print("3. Advanced Payroll (with Bonuses & Deductions)")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            main()
        elif choice == "2":
            batch_calculation()
        elif choice == "3":
            add_bonus_deductions()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid option!")