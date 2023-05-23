document.addEventListener("readystatechange", () => {
  const form = document.getElementById("form");
  const Name = document.getElementById("Name");
  const id = document.getElementById("id");
  const email = document.getElementById("email");
  const phoneNumber = document.getElementById("phoneNumber");
  const address = document.getElementById("address");
  const errorElement = document.getElementById("error");
  const approvedVacations = document.getElementById("approvedVacations");
  const availableVacations = document.getElementById("availableVacations");
  const approvedVacationsValue = approvedVacations.value.trim();
  const availableVacationsValue = availableVacations.value.trim();
  const salary = document.getElementById("salary");
  const salaryValue = salary.value.trim();
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    validateInputs();
  });

  const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector(".error");

    errorDisplay.innerText = message;
    inputControl.classList.add("error");
    inputControl.classList.remove("success");
  };

  const setSuccess = (element) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector(".error");

    errorDisplay.innerText = "";
    inputControl.classList.add("success");
    inputControl.classList.remove("error");
  };

  const isValidEmail = (email) => {
    const re =
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
  };

  const validateInputs = () => {
    const NameValue = Name.value.trim();
    const emailValue = email.value.trim();
    const phoneNumberValue = phoneNumber.value.trim();
    const idValue = id.value.trim();
    const addressValue = address.value.trim();

    if (NameValue === "") {
      setError(Name, "name is required");
    } else {
      setSuccess(Name);
    }

    if (emailValue === "") {
      setError(email, "Email is required");
    } else if (!isValidEmail(emailValue)) {
      setError(email, "Provide a valid email address");
    } else {
      setSuccess(email);
    }

    if (idValue === "") {
      setError(id, "id is required");
    } else if (idValue.length != 8) {
      setError(id, "id must equal 8 numbers.");
    } else {
      setSuccess(id);
    }

    if (phoneNumberValue === "") {
      setError(phoneNumber, "phone Number is required");
    } else if (phoneNumberValue.length != 11) {
      setError(phoneNumber, "phone number must be at least 11 numbers.");
    } else {
      setSuccess(phoneNumber);
    }

    if (addressValue === "") {
      setError(address, "address is required");
    } else {
      setSuccess(address);
    }

    if (approvedVacationsValue === "") {
      setError(approvedVacations, "approved Vacations is required");
    } else {
      setSuccess(approvedVacations);
    }

    if (availableVacationsValue === "") {
      setError(availableVacations, "available Vacations is required");
    } else {
      setSuccess(availableVacations);
    }

    if (salaryValue === "") {
      setError(salary, "salary is required");
    } else {
      setSuccess(salary);
    }
  };
});
