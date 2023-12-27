from create_tables import create_tables
import streamlit as st
from database_functions import add_subbtask, add_task, get_task, get_tasks, delete_task


def st_get_tasks():
    tasks = get_tasks()

    if tasks:
        st.write('Tasks')
        for task in tasks:
            st.write(task)
    else:
        st.write("There are no available tasks")

def st_add_task():
    st.header("Create Task")
    title = st.text_input("Title:")
    detail = st.text_area("Detail:")
    urgency = st.slider("Urgency", min_value=1, max_value=5, value=1)

    col1, col2 = st.columns(2, gap="small")

    with col1:
        if st.button("Add Task"):
            add_task(title, detail, urgency)
            st.success("Task created successfully!")
    
    # with col2:
    #     print("")

    with col2:
        if st.button("Add Subtask"):
            print("")

def st_add_subtask():
    pass

def st_get_task():
    pass

def st_delete_task():
    pass


def main():
    st.title("Streamlit Task Manager")

    menu = st.sidebar.selectbox("Select an action", ["Add Task", "Update Task", "View All Tasks", "View Single Task"])

    if menu == "Add Task":
        st_add_task()
        

if __name__ == "__main__":
    create_tables()
    main()