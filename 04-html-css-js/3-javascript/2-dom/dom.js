// -----------------------------------
// Document Object Model Selection
// -----------------------------------
const title = document.getElementById("title");
title.textContent = "Welcome";                  // --> changing the title

// -----------------------------------
// Event Listeners
// -----------------------------------
const btn = document.getElementById("btn");
btn.addEventListener("click", () => {              // --> event listeners or clicking, hover, key press \, etc.
    alert("Button clicked");                       // --> alaert opens pop up
});

// -----------------------------------
// Forms
// -----------------------------------
document.getElementById("save").addEventListener("click", () => {
    const name = document.getElementById("name").value;
    console.log(name);
});