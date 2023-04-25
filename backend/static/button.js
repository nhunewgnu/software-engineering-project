const loginBtn = document.getElementById("login-btn");

loginBtn.addEventListener("click", () => {
    window.location.href = "login.html";
  });


logoutBtn.addEventListener("click", () => {
    localStorage.removeItem("username");
    updateUI();
  });

  function updateUI() {
    const username = localStorage.getItem("username");
    if (username) {
      userInfo.style.display = "block";
      authOptions.style.display = "none";
      usernameDisplay.textContent = username;
    } else {
      userInfo.style.display = "none";
      authOptions.style.display = "block";
    }
  }
  
  updateUI();