from fastapi import FastAPI

app = FastAPI()

all_todos = [
    {'todo_id': 1, 'todo_name': 'Sports', 'todo_description': 'Go to the gym'},
    {'todo_id': 2, 'todo_name': 'Read', 'todo_description': 'Read 10 pages'},
    {'todo_id': 3, 'todo_name': 'Shop', 'todo_description': 'Go shopping'},
    {'todo_id': 4, 'todo_name': 'Study', 'todo_description': 'Study for exam'},
    {'todo_id': 5, 'todo_name': 'Meditate', 'todo_description': 'Meditate 20 minutes'}
]

@app.get('/')  # static route
def index():
    return {"message": "Hello World"}

# @app.get('/todos')  # static route
# def all_todos():
#     return all_todos

@app.get('/todo/{todo_id}') # path params
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {"result": todo}

@app.get('/todos')  # query params. Run with http://127.0.0.1:9999/todos?first_n=3
def get_all_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    return all_todos


# Post Methods (Try it out with swagger UI or curl)

@app.post('/todos')
def create_todo(new_todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1

    new_todo = {
        'todo_id' : new_todo_id,
        'todo_name' : new_todo['todo_name'],
        'todo_description' : new_todo['todo_description']
    }

    all_todos.append(new_todo)

    return new_todo