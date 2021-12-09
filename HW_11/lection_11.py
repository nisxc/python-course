from os import extsep
import sqlite3

TABLE_CREATE_SQL = '''
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    priority INTEGER NOT NULL);
'''
TASK_INSERT_SQL = '''INSERT INTO tasks (name, priority) VALUES (?,?)'''
TASKS_SELECT_SQL = '''SELECT * FROM tasks'''
TASKS_UPDATE_WHERE_SQL = '''UPDATE tasks SET priority = ? WHERE id = ?'''
TASKS_DELETE_WHERE_SQL = '''DELETE FROM tasks WHERE id = ?'''
# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute(TABLE_CREATE_SQL)
# task_list = [("HELLO", 200), ("HELLO", 210), ("HELLO", 220)]
# c.executemany(TASK_INSERT_SQL, task_list)
# conn.commit()
# conn.close()


class Task:
    def __init__(self):
        self.__task_name = None
        self.__task_priority = None


class TaskManager(Task):
    def __init__(self):
        super().__init__()
        self.__user_input = input('Enter table name: ')
        self.__db_name = self.__user_input + '.db' if len(
            self.__user_input) else self.ErrorBounder()
        self.command = None

    def table_create(self):
        self.__db_init = sqlite3.connect(self.__db_name)
        self.__db_cursor = self.__db_init.cursor()
        self.__db_cursor.execute(TABLE_CREATE_SQL)

    def add_task(self):
        self.__task_name = str(input('Enter task name: '))
        if not len(self.__task_name.strip()):
            raise Exception

        if self.find_task(self.__task_name):
            raise Exception

        self.__task_priority = input('Enter task priority: ')

        if not len(str(self.__task_priority).strip() or self.__task_priority < 1):
            raise Exception

        self.__db_cursor.execute(
            TASK_INSERT_SQL, (self.__task_name, self.__task_priority))
        self.__db_init.commit()
        self.command = input('Are you want exit? ')

    def find_task(self, name):
        for row in self.__db_cursor.execute(TASKS_SELECT_SQL):
            if row == name:
                return True
        return False

    def update_task(self):
        for task in self.show_tasks():
            print('ID:', task[0], ' | ', 'NAME:',
                  task[1], ' | ', 'PRIORITY:', task[2])
        input_id = int(input('Enter id of task, that you want to update: '))
        if input_id:
            input_priority = int(input('Enter new priority value: '))
            if input_priority:
                self.__db_cursor.execute(
                    TASKS_UPDATE_WHERE_SQL, (input_priority, input_id))
                self.__db_init.commit()
                self.command = input('Are you want exit? ')

    def delete_task(self):
        for task in self.show_tasks():
            print('ID:', task[0], ' | ', 'NAME:',
                  task[1], ' | ', 'PRIORITY:', task[2])
        input_id = int(input('Enter id of task, that you want to delete: '))
        if input_id:
            if input_id < 1:
                raise Exception
            self.__db_cursor.execute(
                TASKS_DELETE_WHERE_SQL, (input_id,))
            self.__db_init.commit()
            self.command = input('Are you want exit? ')

    def show_tasks(self):
        return self.__db_cursor.execute(TASKS_SELECT_SQL)

    def ErrorBounder(self):
        raise Exception


try:
    taskManager = TaskManager()
    taskManager.table_create()
    while True:
        if taskManager.command in ['y', 'yes'] and taskManager.command != None:
            break
        # taskManager.add_task()
        # taskManager.update_task()
        taskManager.delete_task()
    for task in taskManager.show_tasks():
        print('ID:', task[0], ' | ', 'NAME:',
              task[1], ' | ', 'PRIORITY:', task[2])
except Exception as Ex:
    print('Error')
