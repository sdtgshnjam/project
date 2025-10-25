import json 

import os

TASK_FILE = "salah.json"
def load_tasks():
    if not os.path.exists(TASK_FILE):
       return []
    with open(TASK_FILE) as f:
        return json.load(f)
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=6)

def add_tasks(titil, status="pendimg"):
    tasks = load_tasks()
    tasks = input("حط اسمك:\n")
    tasks = int(input("عمرك:\n"))
    password = float(int(input("حط الرمز")))
    
    print(f"نورت بأول يوم تدريب{tasks},{tasks}")
