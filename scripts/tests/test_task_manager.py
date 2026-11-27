from scripts.task_manager import TaskManager

def test_add_and_complete_task():
    #Arrange
    tm = TaskManager()

    #Act
    tm.add_task("Напечь блинов")
    assert tm.tasks[0] == {"description" : "Напечь блинов", "completed" : False}

    tm.complete_task(0)
    #Assert
    assert tm.tasks[0] == {"description" : "Напечь блинов", "completed" : True}


def test_remove_task():
    tm = TaskManager()

    tm.add_task("Сварить гречку")
    assert tm.tasks[0] == {"description" : "Сварить гречку", "completed" : False}
    tm.add_task("Напечь блинов")
    assert tm.tasks[1] == {"description": "Напечь блинов", "completed": False}

    tm.remove_task(0)
    assert tm.tasks[0] == {"description": "Напечь блинов", "completed": False}
    assert len(tm.tasks) == 1

def test_save_and_load_task(tmp_path):
    file_name = tmp_path / "tasks.json"
    tm = TaskManager()
    tm.add_task("Сварить гречку")
    tm.add_task("Напечь блинов")
    tm.complete_task(1)

    tm.save_to_json(file_name)
    assert file_name.is_file()


    tm_loaded = TaskManager()
    tm_loaded.load_from_json(file_name)
    assert tm.tasks == tm_loaded.tasks

