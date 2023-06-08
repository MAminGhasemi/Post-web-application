
function validateForm(event) {
   
  
 
    let emailInput = document.getElementsByName("email")[0];
    let passwordInput = document.getElementsByName("password")[0];
  

    let isFormValid = true;


   
    emailInput.classList.remove("error");
    passwordInput.classList.remove("error");
  

    


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

    let passwordStrengthRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[a-zA-Z\d\W_]{8,}$/;
    if (!passwordStrengthRegex.test(passwordInput.value)) {
        passwordInput.classList.add("error");
        passwordError.textContent = "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one symbol.";
        passwordError.classList.add("error");
        isFormValid = false;
        passwordInput.value = "";
    } else {
       
        passwordError.textContent = "";
        passwordError.classList.remove("error");
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




  