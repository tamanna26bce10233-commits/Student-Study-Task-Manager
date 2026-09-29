def validate_task_title(title):
    title = title.strip()

    if not title:
        return False, "Task title cannot be empty."

    if len(title) > 100:
        return False, "Task title must be 100 characters or fewer."

    return True, title
