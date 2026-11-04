class ToDoList:
    def __init__(self):
        self.tasks = dict()


    def add_task(self, task):
        if isinstance(task, str):
            self.tasks[task] = "◯"
        else:
            print("[add_task] : Only string values are allowed")
            return None


    def complete_task(self, task):
        if task in self.tasks:
            self.tasks[task] = "☑"
        else:
            print(f"[complete_task] : Task '{task}' not found")


    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
        else:
            print(f"[remove_task] : Task '{task}' not found")


    def list_tasks(self):
        print("[list_tasks] : ", self.tasks)


my_todo_list = ToDoList()
my_todo_list.list_tasks()
my_todo_list.add_task("Task 1")
my_todo_list.add_task("Task 2")
my_todo_list.add_task(2)
my_todo_list.list_tasks()
my_todo_list.complete_task("Task 2")
my_todo_list.list_tasks()
my_todo_list.remove_task("Task 2")
my_todo_list.remove_task("Task 4")
my_todo_list.list_tasks()
