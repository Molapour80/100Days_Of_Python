##Calculates 
def main():
    print("Welcom to Calulate:))")
    print("1:Submit")
    print("2:minus")
    print("3:Multiplication")
    print("4:Division")
    print("5:Exit")


    while True:
        choose = input("Enter your function:").strip()
        if choose == "1":
            a = int(input("Enter your number1:"))
            b = int(input("Enter your number2:"))
            sub = a + b
            print(sub)

        elif choose == "2":
            a = int(input("Enter your number1:"))
            b = int(input("Enter your number2:"))
            min_ = a - b
            print(min_)

        elif choose == "3" :
            a = int(input("Enter your number1:"))
            b = int(input("Enter your number2:"))
            Milti = a * b
            print(Milti)

        elif choose == "4":
            a = int(input("Enter your number1:"))
            b = int(input("Enter your number2:"))
            if b == 0 :
                print("not true")
            else:
                dis = a / b
                print(dis)

        elif choose == "":
            continue

        elif choose == "6":
            break


main()




