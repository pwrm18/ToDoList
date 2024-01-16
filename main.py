user_prompt = "Type 'add', 'show', 'edit', 'complete' or 'exit':"
file = open("todos.txt", 'r')
todos = file.readlines()
file.close()

while True:
    action = input(user_prompt).strip()
    match action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            for  index, todo in enumerate(todos):
                todo = todo.strip("\n")
                print(f"{index + 1}: {todo}")
        case "exit":
            break
        case "complete":
            number = int(input("Which position you want to complete? Write a number: "))
            todos.pop(number - 1)
        case "edit":
            number = int(input("Which position you want to edit? Write a number: "))
            new_todo = input("Write a new text for a position: ")
            todos[number - 1] = new_todo
        case _:
            print("idk what you just printed!")

print("Bye!")