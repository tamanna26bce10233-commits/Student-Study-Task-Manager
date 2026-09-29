def show_progress(tasks):
    total = len(tasks)
    completed = 0

    for task in tasks:
        if task.completed:
            completed += 1

    print("Total tasks:", total)
    print("Completed tasks:", completed)

    if total > 0:
        percentage = (completed / total) * 100
        print("Progress:", round(percentage, 2), "%")
    else:
        print("Progress: 0 %")
        