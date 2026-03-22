document.addEventListener('DOMContentLoaded', function() {
    const createTaskButton = document.getElementById('create-task');
    const taskListElement = document.getElementById('task-list');

    createTaskButton.addEventListener('click', function() {
        // Implement task creation logic here
        alert('Create task functionality is not yet implemented.');
    });

    // Fetch tasks and display them
    fetch('/tasks')
        .then(response => response.json())
        .then(tasks => {
            taskListElement.innerHTML = '';
            tasks.forEach(task => {
                const taskElement = document.createElement('div');
                taskElement.textContent = `${task.title} - ${task.description} - ${task.created_at}`;
                taskListElement.appendChild(taskElement);
            });
        })
        .catch(error => {
            console.error('Error fetching tasks:', error);
            taskListElement.textContent = 'Error loading tasks.';
        });
});