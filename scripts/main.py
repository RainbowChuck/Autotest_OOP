class ToDoList:
    def __init__(self):
        self.tasks = dict()


    def add_task(self):
        task = input("[add_task]: Какую задачу добавить?")
        if isinstance(task, str):
            self.tasks[task] = "◯"
        else:
            print("[add_task] : Only string values are allowed")
            return None


    def complete_task(self):
        task = input("[complete_task]: Какую задачу выполнить? ")
        if task in self.tasks:
            self.tasks[task] = "☑"
        else:
            print(f"[complete_task] : Task '{task}' not found")


    def remove_task(self):
        task = input("[remove_task]: Какую задачу убрать? ")
        if task in self.tasks:
            del self.tasks[task]
        else:
            print(f"[remove_task] : Task '{task}' not found")


    def list_tasks(self):
        print("[list_tasks] : ", self.tasks)


def user_interface(todo):
    menu_options = {
        "1" : todo.add_task,
        "2" : todo.remove_task,
        "3" : todo.list_tasks,
        "4" : todo.complete_task
    }
    while True:
        choice = input("[user_interface] : Выберете дейстие: ")

        if choice == "5":
            break

        if choice in menu_options:
            menu_options[choice]()



my_todo_list = ToDoList()
user_interface(my_todo_list)



