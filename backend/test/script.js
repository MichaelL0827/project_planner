async function getData(){
    const request = await fetch('http://localhost:8000/api/read/task-todo/jane_smith');
    const response = await request.json()
    console.log(response);
    const data = response[0].Todos;
    console.log(JSON.parse(data));

}

getData()