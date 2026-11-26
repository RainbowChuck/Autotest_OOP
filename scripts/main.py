class ToDoList:
    def __init__(self):
        self.tasks = {}


    def add_task(self, task):
        if not isinstance(task, str) or not task.strip():
            print("Некорректное название задачи")
            return

        if task in self.tasks:
            print("Такая задача уже существует")
            return

        self.tasks[task] = False


    def complete_task(self, task):
        if task not in self.tasks:
            print(f"Task '{task}' not found")
            return

        self.tasks[task] = True


    def remove_task(self, task):
        if task not in self.tasks:
            print(f"Task '{task}' not found")
            return

        del self.tasks[task]


    def list_tasks(self):
        for task, status in self.tasks.items():
            print(f"{'☑' if status else '◯'} {task}")


def user_interface(todo):
    menu_options = {
        "1": ("Добавить задачу", lambda: todo.add_task(
            input("Какую задачу добавить? ").strip()
        )),
        "2": ("Удалить задачу", lambda: todo.remove_task(
            input("Какую задачу удалить? ").strip()
        )),
        "3": ("Список задач", todo.list_tasks),
        "4": ("Выполнить задачу", lambda: todo.complete_task(
            input("Какую задачу выполнить? ").strip()
        ))
    }


    while True:
        for key, (name, _) in menu_options.items():
            print(f"{key}: {name}")

        print("5: Выход")

        choice = input("Выберите действие: ")

        if choice == "5":
            break

        if choice in menu_options:
            menu_options[choice][1]()
        else:
            print("Неизвестная команда")


my_todo_list = ToDoList()
user_interface(my_todo_list)



