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
        pass

    elif command == "delete":
        pass

    elif command == "mark-in-progress":
        pass

    elif command == "mark-done":
        pass

    else:
        print("invalid command")


if __name__ == "__main__":
    main()