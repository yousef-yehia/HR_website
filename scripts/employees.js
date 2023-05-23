const searchButton = document.getElementById("search");
const searchInput = document.getElementById("search-input");
const table = document.getElementById("table");
const rows = Array.from(table.rows);

searchButton.addEventListener("click", () => {
  const searchValue = searchInput.value;
  const filtered = rows.filter((row) => {
    return row.cells[1].innerText
      .toLowerCase()
      .includes(searchValue.toLowerCase());
  });
  table.innerHTML = "";
  filtered.forEach((row) => {
    table.appendChild(row);
  });
});
function Get() {
  let http = new XMLHttpRequest();
  function callBack() {
    if (4 === http.readyState && (http.status === 201 || http.status === 200)) {
      var responseBody = JSON.parse(http.responseText);
      console.log(responseBody);
    } else if (http.status === 404) {
      console.log("Not Found");
    } else if (http.status === 400) {
      var responseBody = JSON.parse(
        http.responseText ?? '{"error":"Un expectedError"}'
      );
      console.log("Some data is missing");
      console.log(responseBody);
    }
  }
  http.onreadystatechange = callBack;
  http.open("GET", "http://127.0.0.1:8000/employees");
  http.send();
}

function GetEmployee() {
  const testEmployee = {
    name: "Name",
    email: "email@gmail.com",
    phoneNumber: "01094046206",
    dateOfBirth: "2006-07-21",
    gender: "Male",
    maritalStatus: "Married",
    address: "6th of october city",
    availableVacations: 100,
    salary: 10000,
  };

  Get(testEmployee);
}