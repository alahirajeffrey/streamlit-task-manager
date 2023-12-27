from database import create_connection

def add_task(title, detail, urgency=1):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO tasks (title, detail, urgency) VALUES (?, ?, ?)
        """,
        (title, detail, urgency)
    )
    connection.commit()
    cursor.close()

def add_subbtask(title, detail, task_id, urgency=1):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO subtasks (title, detail, urgency, task_id) VALUES (?, ?, ?, ?)
        """,
        (title, detail, urgency, task_id)
    )
    connection.commit()
    cursor.close()

def get_tasks():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM tasks
        """
    )
    tasks = cursor.fetchall()

    connection.commit()
    cursor.close()
    return tasks

def get_task(task_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM tasks WHERE id = ?
        """, (task_id,))
    task = cursor.fetchone()
    
    if task:
        cursor.execute("SELECT * FROM subtasks WHERE task_id = ?", (task_id,))
        subtasks = cursor.fetchone()
        task_with_subtasks = {'task': task, 'subtasks': subtasks}
    else:
        return 

    cursor.close()
    return task_with_subtasks

def delete_task(task_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE * FROM tasks WHERE id = ?", (task_id,))
    cursor.close()
    return 
