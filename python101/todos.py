todos = []

# Prompt the user the first time
new_todo = input("What do you need to do? ")
while len(new_todo) > 0:
    todos.append(new_todo)

    # Print the current list of to-do items
    print("To do:")
    print("====================")
    count = 1
    for todo in todos:
        print("%d: %s" % (count, todo))
        count += 1

    # Prompt the user again
    print("\n")
    new_todo = input("What do you need to do? ")

print("Have a nice day!")