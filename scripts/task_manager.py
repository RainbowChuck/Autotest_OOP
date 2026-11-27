import json
import pytest



class TaskManager:
    def __init__(self):
        self.tasks = []


    def _is_valid_index(self, index: int):
        return type(index) is int and 0 <= index < len(self.tasks)


    def add_task(self, description:str):
        self.tasks.append({"description" : description,
        "completed" : False})


    def complete_task(self, index: int):
        if not self._is_valid_index(index):
            print("некорректный индекс")
            return

        self.tasks[index]["completed"] = True


    def remove_task(self, index: int):
        if not self._is_valid_index(index):
            print("некорректный индекс")
            return

        self.tasks.pop(index)


    def save_to_json(self, filename: str):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)


    def load_from_json(self, filename: str):
        with open(filename, "r") as file:
            self.tasks = json.load(file)


    def show_tasks(self):
        for task in self.tasks:
            print(task)


