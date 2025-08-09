def tasks():
    tasks = []  #empty list//
    print("---WELCOME TO TO DO LIST MANAGER---")

    total_task = int(input("ENTER THE NUMBER OF TASKS YOU WANT TO ADD:"))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}:\n >>>")
        tasks.append(task_name)

    print(f"TODAY'S TASKS ARE:\n{tasks}\n")


    while True:
            print("---MENU---")
            operation = int(input("ENTER\n1 to ADD\n2 to UPDATE\n3 to DELETE\n4 to VIEW\n5 to EXIT\n>>>"))
            if operation == 1:
                add = input ("enter the task:\n>>>")
                tasks.append(add)
                print(f"task'{add}'has been successfully added..!")

            elif operation == 2:
                updated_task = input ("enter the task you want to update:")
                if updated_task in tasks:
                 upd = input ('enter the new task:')
                idx = tasks.index(updated_task)
                tasks[idx] = upd
                print(f"{upd} is successfully updated..!")

            elif operation == 3 :
                del_val = input("enter the task you want to delete:")
                if del_val in tasks :
                    idx = tasks.index(del_val)
                del tasks[idx]
                print(f"task {del_val} has been deleted...")


            elif operation == 4 :
                print(f"total tasks :{tasks}")


            elif operation == 5:
                print("closing the program .....!")
                break

            else:
                print("INVALID INPUT !\nPLEASE ENTER A VALID ONE.\n")
              

                print("THANK YOU !\n")
tasks()         # calling the function//