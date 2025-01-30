from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__) 
TASK_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            content = file.read()
            return json.loads(content) if content.strip() else []
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())

@app.route('/add', methods=['POST'])
def add_task():
    tasks = load_tasks()
    data = request.json
    new_task = {'id': len(tasks) + 1, 'text': data['text'], 'done': False}
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task)

@app.route('/remove/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return jsonify({'message': 'Task removed'})

@app.route('/mark/<int:task_id>', methods=['PATCH'])
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
    save_tasks(tasks)
    return jsonify({'message': 'Task updated'})

if __name__  == '__main__':
    app.run(debug=True)