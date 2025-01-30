document.addEventListener('DOMContentLoaded', loadTasks);

function loadTasks() {
    fetch('/tasks')
        .then(response => response.json())
        .then(tasks => {
            const taskList = document.getElementById('taskList');
            taskList.innerHTML = '';
            tasks.forEach(task => {
                let li = document.createElement('li');
                li.textContent = task.text;
                li.className = task.done ? 'completed' : '';
                li.onclick = () => markTask(task.id);

                let removeBtn = document.createElement('button');
                removeBtn.textContent = 'X';
                removeBtn.onclick = (e) => {
                    e.stopPropagation();
                    removeTask(task.id);
                };
                li.appendChild(removeBtn);
                taskList.appendChild(li);
            });
        });
}

function addTask() {
    let taskText = document.getElementById('taskInput').value;
    if (!taskText) return;

    fetch('/add', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text: taskText})
    }).then(() => {
        document.getElementById('taskInput').value = '';
        loadTasks();
    });
}

function removeTask(taskId) {
    fetch(`/remove/${taskId}`, {method: 'DELETE'})
        .then(() => loadTasks());
}

function markTask(taskId) {
    fetch(`/mark/${taskId}`, {method: 'PATCH'})
        .then(() => loadTasks());
}


























