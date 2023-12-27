from database import create_connection

def create_task(title, detail, urgency=1):
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