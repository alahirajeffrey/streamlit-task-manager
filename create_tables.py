from database import create_connection

def create_tables():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY  AUTOINCREMENT,
            title TEXT NOT NULL,
            detail TEXT NOT NULL,
            urgency INTEGER DEFAULT 1 CHECK (urgency>=1 AND urgency <=5),
            is_completed INTEGER DEFAULT 0,
            date_created DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subtasks (
            id INTEGER PRIMARY KEY  AUTOINCREMENT,
            task_id INTEGER,
            subtask_title  TEXT NOT NULL,
            subtask_details  TEXT NOT NULL,
            subtask_urgency INTEGER DEFAULT 1 CHECK (subtask_urgency>=1 AND subtask_urgency <=5),
            is_completed INTEGER DEFAULT 0,
            date_created DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()
