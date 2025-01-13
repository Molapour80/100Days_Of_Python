task = []

def add_work():

    name_work = input("Enter your task :")
    task.append(name_work)
    return f"add the {name_work}"

def remove_work():
    if task :

        try:

            ch = input("Enter your work:")
            if ch in task:
                task.remove(ch)
                return f"removed the {ch} in {task}"
            return f"not found {ch}" 
            
        except:
            raise ValueError 

def display():

    if  not task:
        print("Empty")
    else:
        print("List work:")
        for index , name in enumerate(task)  :
            print(f"{index +1} : {name}")
    

def main():

    while True:

        print("1:Add work")
        print("2:remove work")
        print("3:Display")
        print("4:Exit")

        try:

            choses =input("Choses the work:")
            if choses == "1":
                add_work()

            elif choses == "2":
                remove_work()
            
            elif choses == "3":
                display()

            elif choses == "4":
                break

            elif choses == " ":
                continue

        except:
            return "ERROR"
        
main()
