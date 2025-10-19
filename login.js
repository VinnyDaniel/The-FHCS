const loginForm = document.getElementById("login-form");
const loginContainer = document.getElementById("login-container");
const logoContainer = document.getElementById("logo-container");

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  // Hide login and show logo animation
  loginContainer.style.opacity = "0";

  setTimeout(() => {
    loginContainer.style.display = "none";
    logoContainer.style.display = "flex";
  }, 600);
});
