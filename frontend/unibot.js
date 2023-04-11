const loginBtn = document.getElementById("login-btn");

function sendMessage() {
    var inputField = document.querySelector(".input");
    var messageText = inputField.value;
    var chatBox = document.querySelector(".box");

    // Display user message in chat box
    var userMsg = document.createElement("div");
    userMsg.classList.add("item", "right");
    userMsg.innerHTML = '<div class="msg"><p>' + messageText + '</p></div>';
    chatBox.appendChild(userMsg);

    // Send message using AJAX
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/chat_bot");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.onload = function() {
        if (xhr.status === 200) {
            var botMsg = document.createElement("div");
            botMsg.classList.add("item");
            botMsg.innerHTML = '<div class="icon"><i class="fa fa-user"></i></div><div class="msg"><p>' + xhr.responseText + '</p></div>';
            chatBox.appendChild(botMsg);
            inputField.value = "";
        }
    };
    xhr.send(JSON.stringify({message: messageText}));
}

var inputField = document.querySelector(".input");
inputField.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

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