import sys
import json 
import os 
from datetime import datetime



TASK_FILE = "tasks.json"

# bagian task adding
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


# fungsi mark task (mark-in-progress, mark-done) --> menggunakan find_task_by_id function
def mark_task(status_task, task_id):
    task = load_task()
    found_task = find_task_by_id(task, task_id)

    if not found_task:
        print("Task Tidak Ditemukan")

    if status_task == 'mark-in-progress':
        found_task[0]['status'] = 'in-progress'
        found_task[0]['updatedAt'] = datetime.now().isoformat()

        save_task(task)
        print("Status Task berhasil diubah (in-progress)✅")

    elif status_task == "mark-done":
        found_task[0]['status'] = 'done'
        found_task[0]['updatedAt'] = datetime.now().isoformat()

        save_task(task)
        print("Status Task berhasil diubah (done)✅")
    

# Fungsi List Task (todo - in progress - done)
def list_task(status_filter=None):
    task = load_task()

    if not task:
        print("Task Kosong")
    
    else:

        if status_filter == "todo":
            todo_task = [field for field in task if field['status'] == 'todo']
            for task in todo_task:
                print(f"{task['id']}. {task['description']} | {task['status']}")

        elif status_filter == "done":
            done_task = [field for field in task if field['status'] == 'done']
            for task in done_task:
                print(f"{task['id']}. {task['description']} | {task['status']}")

        elif status_filter == "in-progress":
            in_progress_task = [field for field in task if field['status'] == "in-progress"]
            for task in in_progress_task:
                print(f"{task['id']}. {task['description']} | {task['status']}")

        else:
            for tsk in task:
                print(f"{tsk['id']}. {tsk['description']} | {tsk['status']}")


# main app
def main():
    args = sys.argv[1:]

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
            list_task(args[1])
        else:
            try:
                list_task()

            except:
                print("Gagal Eksekusi List Task")

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
        try:
            mark_task(args[0], args[1])
        
        except:
            print("Gagal mark-in-progress Task")

    elif command == "mark-done":
        try:
            mark_task(args[0], args[1])
        
        except:
            print("Gagal mark-done task")

    else:
        print("invalid command")


if __name__ == "__main__":
    main()