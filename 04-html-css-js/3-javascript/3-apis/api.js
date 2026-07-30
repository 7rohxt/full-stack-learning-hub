// -----------------------------------
// Fetch (GET) — matches:
//   @app.get("/hello")
//   def hello():
//       return {"message": "Hello"}
// -----------------------------------
fetch("http://localhost:8000/hello")
    .then(response => response.json())
    .then(data => {
        console.log("GET /hello ->", data);
    });


// -----------------------------------
// async / await — same GET as above, cleaner syntax
// (this is the style you'll actually use in React)
// -----------------------------------
async function getUsers() {
    const response = await fetch("http://localhost:8000/hello");
    const data = await response.json();
    console.log("async/await ->", data);
}

getUsers();


// -----------------------------------
// POST Request — matches:
//   @app.post("/users")
//   def create_user(user: User):
//       return user
// -----------------------------------
fetch("http://localhost:8000/users", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: "Rohit",
        age: 24
    })
})
    .then(res => res.json())
    .then(data => {
        console.log("POST /users ->", data);
    });

