
function validateForm(event) {
   
  
    let usernameInput = document.getElementsByName("username")[0];
    let emailInput = document.getElementsByName("email")[0];
    let passwordInput = document.getElementsByName("password")[0];
    let confirmPasswordInput = document.getElementsByName("confirm-password")[0];

    let isFormValid = true;


    usernameInput.classList.remove("error");
    emailInput.classList.remove("error");
    passwordInput.classList.remove("error");
    confirmPasswordInput.classList.remove("error");

    let usernameError = document.getElementById("username-error");

    if (usernameInput.value.length < 3 || usernameInput.value.length > 25) {
        usernameInput.classList.add("error");
        usernameInput.value = "";
        usernameError.textContent = "Username must be between 3 and 25 characters long.";
        usernameError.classList.add("error");
        isFormValid = false;
    } else {
        
        usernameError.textContent = "";
        usernameError.classList.remove("error");
    }


    let emailError = document.getElementById("email-error");

    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailInput.value)) {
        emailInput.classList.add("error");
        emailError.textContent = "Invalid email address.";
        emailError.classList.add("error");
        emailInput.value = "";
        isFormValid = false;
    } else {
        
        emailError.textContent = "";
        emailError.classList.remove("error");
    }

    let passwordError = document.getElementById("password-error");
    let passtemp=passwordInput.value
    let passwordStrengthRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[a-zA-Z\d\W_]{8,}$/;
    if (!passwordStrengthRegex.test(passwordInput.value)) {
        passwordInput.classList.add("error");
        passwordError.textContent = "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one symbol.";
        passwordError.classList.add("error");
        isFormValid = false;
        passtemp=passwordInput.value
        passwordInput.value = "";
    } else {
       
        passwordError.textContent = "";
        passwordError.classList.remove("error");
    }
    console.log(passwordInput.value)
    let confirmPasswordError = document.getElementById("confirm-password-error");
    console.log(confirmPasswordInput.value)
    if (passtemp !== confirmPasswordInput.value) {
        confirmPasswordInput.classList.add("error");
        confirmPasswordError.textContent = "Passwords do not match.";
        confirmPasswordError.classList.add("error");
        isFormValid = false;
        confirmPasswordInput.value = "";
    } else {
       if(passwordInput.value===""){
        confirmPasswordInput.value = "";
       }
        confirmPasswordError.textContent = "";
        confirmPasswordError.classList.remove("error");
    }

    if (!isFormValid) {
        event.preventDefault(); // Prevent form submission
    }
    
}
const myForm = document.getElementById("form");

myForm.addEventListener("submit", function(event) {
  validateForm(event);
});
// let form = document.getElementById("form");
// form.addEventListener("submit", validateForm);




  