document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("eventForm");
    const addTodoButton = document.getElementById("addTodo");
    const todoContainer = document.getElementById("todoContainer");
    let todoCount = 0;

    // Add new Todo item
    addTodoButton.addEventListener("click", () => {   // Line 10
        const todoDiv = document.createElement("div");
        todoDiv.classList.add("todo-item");
        todoDiv.innerHTML = `
            <label>Todo Name:</label>
            <input type="text" name="todoName${todoCount}" required>

            <label>Description:</label>
            <textarea name="todoDescription${todoCount}" required></textarea>

            <label>Start Date:</label>
            <input type="date" name="todoStart${todoCount}" required>

            <label>End Date:</label>
            <input type="date" name="todoEnd${todoCount}" required>

            <button type="button" class="removeTodo">Remove</button>
        `;
        todoContainer.appendChild(todoDiv);

        // Fix: Add remove functionality
        todoDiv.querySelector(".removeTodo").addEventListener("click", () => {   // Line 28
            todoDiv.remove();
        });

        todoCount++;
    });

    // Handle form submission
    form.addEventListener("submit", async (e) => {   // Line 35
        e.preventDefault();

        const taskName = document.getElementById("eventName").value.trim();
        const taskDescription = document.getElementById("eventDescription").value.trim();
        const username = "testUser"; // Replace with actual username from authentication

        // Fix: Validate input fields before submitting
        if (!taskName || !taskDescription) {   // Line 41
            alert("Please fill in all required fields.");
            return;
        }

        // Fix: Fetch Task ID dynamically
        const taskResponse = await fetch("http://127.0.0.1:8000/task", {   // Line 46
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ 
                Name: taskName, 
                Description: taskDescription, 
                Username: username 
            }),
        });

        if (!taskResponse.ok) {   // Error Handling - Line 54
            alert("Error creating task!");
            return;
        }

        const taskData = await taskResponse.json();  // Fix: Extract Task ID - Line 58
        const taskId = taskData.id; 

        // Loop through todos and validate them before sending - Line 61
        const todoItems = document.querySelectorAll(".todo-item");
        for (let item of todoItems) {
            const todoName = item.querySelector("input[name^='todoName']").value.trim();
            const todoDescription = item.querySelector("textarea[name^='todoDescription']").value.trim();
            const startDate = item.querySelector("input[name^='todoStart']").value;
            const endDate = item.querySelector("input[name^='todoEnd']").value;

            if (!todoName || !todoDescription || !startDate || !endDate) {   // 🔹 Validate todo fields - Line 68
                alert("Please complete all fields for each todo.");
                return;
            }

            await fetch("http://127.0.0.1:8000/todo", {   // 🔹 Line 73
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ 
                    Name: todoName, 
                    Description: todoDescription, 
                    Completed: false, 
                    Start: startDate, 
                    End: endDate, 
                    TaskId: taskId 
                }),
            });
        }

        alert("Event created successfully!");   // Success message - Line 85
        form.reset();
        todoContainer.innerHTML = "";
    });
});
