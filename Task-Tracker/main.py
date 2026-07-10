import sys
import json 
import os 
from datetime import datetime


# bagian task adding
TASK_FILE = "tasks.json"

def load_task():
    if not os.path.exists(TASK_FILE):
        return []
    
    with open(TASK_FILE, 'r') as f:
        task = json.load(f)

    return task


def save_task(task):
    with open(TASK_FILE, "w") as f:
        json.dump(task, f, indent=4)



def get_next_id(task):
    if not task:
        return 1
    
    return max([field['id'] for field in task])+1

def add_task(description):
    task = load_task()
    new_id = get_next_id(task)

    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),

    }


    task.append(new_task)
    save_task(task)
    print(f"task added successfully (ID: {new_id})✅")


# Bagian untuk update dan delete task
# karena kedua task ini butuh mencari task sebagai target task, maka dibuat satu fungsi helper task pencarian

def find_task_by_id(task_list, target_id):
    if not task_list:
        print("Task masih kosong")

    else:

        target_task = [field for field in task_list if field['id'] == int(target_id)]

        if not target_task:
            print("Task Tidak ditemukan")

        else:
            return target_task


# fungsi update task -> menggunakan find_task_by_id function

def update_task(task_id, new_description):
    task = load_task()
    found_task = find_task_by_id(task, task_id)

    found_task[0]['description'] = new_description
    found_task[0]['updatedAt'] = datetime.now().isoformat()

    save_task(task)
    print('Task Berhasil di Update ✅')


# fungsi delete task -> menggunakan find_task_by_id function

def delete_task(task_id):
    tasks = load_task()
    found_task = find_task_by_id(tasks, task_id)


    tasks = [task for task in tasks if task['id'] != found_task[0]['id']]

    save_task(tasks)
    print("Berhasil Delete Task ✅")


# main app
def main():
    args = sys.argv[1:]
    print(args)

    if len(args) == 0:

        return 
    
    command = args[0]

    if command == "add":
        try:
            add_task(args[1])

        except:
            print("masukkan task yang ingin ditambahkan")
            print("example: add 'Buy groceries'")

    elif command == "list":
        if len(args) > 1:
            pass
        else:
            pass

    elif command == "update":
        try:
            update_task(args[1], args[2])

        except:
            print("Gagal Mengupdate Task")

    elif command == "delete":
        try:
            delete_task(args[1])

        except:
            print("Gagal Delete Task")

    elif command == "mark-in-progress":
        pass

    elif command == "mark-done":
        pass

    else:
        print("invalid command")


if __name__ == "__main__":
    main()