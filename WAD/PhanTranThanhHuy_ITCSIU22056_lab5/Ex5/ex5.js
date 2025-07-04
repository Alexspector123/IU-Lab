const todoList = JSON.parse(localStorage.getItem('todoList') || []);

renderTodoList();

function renderTodoList() {
    let todoListHTML = '';

    todoList.forEach((value, index) => {
        const {name, done} = value;

        const doneClass = done ? 'done' : '';
        const iconClass = done ? 'fa-solid fa-square-check' : 'fa-regular fa-square';

        const html = `
            <button class="done-button" data-index="${index}">
                <i class="${iconClass}"></i>
            </button>
            <div class="todo-text ${doneClass}">${name}</div>
            <button class="delete-button" data-index="${index}">
                <i class="fa-solid fa-trash"></i>
            </button>
        `;
        todoListHTML += html;
    });
    
    document.querySelector('.todo-list').innerHTML = todoListHTML;

    document.querySelectorAll('.delete-button')
        .forEach((deleteButton, index) => {
            deleteButton.addEventListener('click',() => {
                todoList.splice(index, 1);
                renderTodoList();
            });
        });


    document.querySelectorAll('.done-button')
        .forEach((doneButton, index) => {
            doneButton.addEventListener('click',() => {
                todoList[index].done = !todoList[index].done;
                renderTodoList();
            });
        });
}

document.querySelector('.submit-button')
    .addEventListener('click', () => {
        addTodo();
    });

function addTodo(){
    let inputName = document.querySelector('.input').value;

    todoList.push({name: inputName});

    localStorage.setItem('todoList', JSON.stringify(todoList));

    document.querySelector('.input').value = '';
    renderTodoList();
}