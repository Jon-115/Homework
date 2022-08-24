TodoList = []
prompt = ""
task = []

while len(TodoList) < 100:
    prompt = input("Press 1 to add task \nPress 2 to delete task\nPress 3 to view all tasks\nPress q to quit\n")
    if (str.isdigit(prompt)==True):
        if int(prompt) == 1:
            title = input("What is the title of the task? ")
            prio = input("What is the priority of the task?(high,medium,or low) ")
            task = [len(TodoList)+1, title , prio]
            TodoList.append(task)
            continue
        elif int(prompt) == 2:
            print(TodoList)
            remove = input("What task would you like to remove? ")
            remove = int(remove)
            TodoList.pop(remove-1)
            i = 0
            for x in TodoList:
                TodoList[i][0]=i+1
                i = i + 1
            continue
        elif int(prompt) == 3:
            print(TodoList)
            break
    elif prompt == "q":
        break
    else:
        continue
print(TodoList)