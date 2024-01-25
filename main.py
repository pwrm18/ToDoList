from functions import read_todos, write_todos


todos = read_todos()
user_prompt = "Type 'add', 'show', 'edit', 'complete' or 'exit':"


while True:
    action = input(user_prompt).strip()
    if action.startswith("add"):
        todo = action[4:]
        todos.append(todo + "\n")
        write_todos(todos)
    elif action.startswith("show"):
        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index + 1}: {todo}")
    elif action.startswith("complete"):
        try:
            number = int(action[9:])
            todos.pop(number - 1)
            write_todos(todos)
        except:
            print("Can't complete that!")
    elif action.startswith("edit"):
        try:
            number = int(action[5:])
            new_todo = input("Write a new text for a position: ")
            todos[number - 1] = new_todo + "\n"
            write_todos(todos)
        except:
            print("Your command is not valid! Type a number!")
    elif action.startswith("exit"):
        break
    else:
        print("idk what you just printed!")

print("Bye!")