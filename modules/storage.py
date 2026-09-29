tasks = []


def add_task(task):
    tasks.append(task)


def get_tasks():
    return tasks


def search_task(keyword):
    found = []

    for task in tasks:
        if keyword.lower() in task.title.lower():
            found.append(task)

    return found


def complete_task(title):
    for task in tasks:
        if task.title.lower() == title.lower():
            task.completed = True
            return True

    return False

        
        