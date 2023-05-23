const myform = document.getElementById("myform");
const id = document.getElementById("id");
const errorElement = document.getElementById("error");
const submitbutton = document.getElementById("btn-submit");
const empName = document.getElementById("Name");
submitbutton.onclick = function () {
  myform.addEventListener("submit", (e) => {
    let messages = [];
    if (id.value == "" || id.value == null) {
      alert("ID is required");
      return false;
    }
    if (id.value.length < 6) {
      alert("ID must be longer than 5 numbers");
      return false;
    }

    if (isNaN(id.value)) {
      alert("ID must only be numbers");
      return false;
    }
    if (empName.value == "" || empName.value == null) {
      alert("employee's name is required");
      return false;
    }

    letters = /^[A-Za-z]+$/;
    if (!empName.value.match(letters)) {
      alert("name must only be characters");
      return false;
    }

    if (messages.length > 0) {
      e.preventDefault();
      errorElement.innerText = messages.join(", ");
    } else {
      return true;
    }
  });
};
