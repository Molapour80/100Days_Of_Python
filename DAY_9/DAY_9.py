##
import json
def load(filename = 'response.json'):
    try:
        with open(filename,'r')as f:
            return json.load(f)
    except (FileNotFoundError ,json.JSONDecodeError):
        return []
    
def save(response,filename = 'response.json'):
    with open(filename, 'w') as f:
        json.dump(response, f, ensure_ascii=False, indent=4)

def display(response):
    if not response:
        print("Not anser :(")
        return
    print("\nresult:")
    for id ,response1 in enumerate(response, start=1):
        print(f"{id}, {response1['name']},{response1['email']},{response1['anser']}")



def main():
    print("Welcom to Survey")
    response = load()

  
    while True:
           
        name = input("Enter your name:")
        email = input("Enter your email: ")
        anser =input("Enter your qusation:")

        response.append({'name':name ,'email':email ,'anser':anser})
        save(response)

        display(response)

        play_again = input("Are you send the another qustion(yes or no):)")
        if play_again != "yes":
             break
    print("thanks for the Survey")

if  __name__ == "__main__":
    main()



       


