import sys


sys.path.insert(0, "modules/storage")
sys.path.insert(0, "modules/logic")
sys.path.insert(0, "modules/ui")


import storage
import logic
import ui


logic.init(storage)


while True:
    ui.show_menu()
    choice = input("👉 Ваш выбор: ")
    
    if choice == "1":
        tasks = logic.get_all()
        ui.show_tasks(tasks)
        input("Нажмите Enter...")
    
    elif choice == "2":
        text = ui.get_task_text()
        if text:
            logic.add(text)
            ui.show_message("Задача добавлена!")
        input("Нажмите Enter...")
    
    elif choice == "3":
        ui.show_tasks(logic.get_all())
        task_id = ui.get_task_id()
        if logic.complete(task_id):
            ui.show_message("Задача выполнена!")
        else:
            ui.show_message("Задача не найдена!")
        input("Нажмите Enter...")
    
    elif choice == "4":
        ui.show_tasks(logic.get_all())
        task_id = ui.get_task_id()
        if logic.delete(task_id):
            ui.show_message("Задача удалена!")
        else:
            ui.show_message("Задача не найдена!")
        input("Нажмите Enter...")
    
    elif choice == "5":
        ui.show_message("До свидания!")
        break
    
    else:
        ui.show_message("Неверный выбор!")
        input("Нажмите Enter...")