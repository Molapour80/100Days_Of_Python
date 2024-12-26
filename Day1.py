import random
#gutss the number
def guess_the_number():
    number = random.randint(1,100)
    attempts = 0 
    choses = 10 #count gutses

    print("Welcom to the game:)")
    print("You have a ten chosess")

    while True:
        chosess = input("Enter your number:")
       
        if not chosess.isdigit():
           print("pleas try agaen!!")
           continue
       
        chosess =int(chosess)
        attempts+= 1

        if chosess < number and attempts <= choses:

           print("upper number")

        elif chosess > number  and attempts <= choses:
            print("lower number")

        elif attempts == choses:
            print("NOT WONN")
            
        else:
            print("you wonn:)))")
            break

def main():
    guess_the_number()


if __name__ == "__main__":
    main()
