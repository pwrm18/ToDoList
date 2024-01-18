user_prompt = "Type 'add', 'show', 'edit', 'complete' or 'exit':"
with open("todos.txt", 'r') as file:
    todos = file.readlines()

while True:
    action = input(user_prompt).strip()
    if action.startswith("add"):
        todo = action[4:]
        todos.append(todo)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif action.startswith("show"):
        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index + 1}: {todo}")
    elif action.startswith("complete"):
        try:
            number = int(action[9:])
            todos.pop(number - 1)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except:
            print("Can't complete that!")
    elif action.startswith("edit"):
        try:
            number = int(action[5:])
            new_todo = input("Write a new text for a position: ")
            todos[number - 1] = new_todo
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except:
            print("Your command is not valid! Type a number!")
    elif action.startswith("exit"):
        break
    else:
        print("idk what you just printed!")

print("Bye!")