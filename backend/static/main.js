const messages = document.querySelector(".messages");
const messageForm = document.querySelector("#message-form");
const input = document.querySelector("#message");

messageForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value;
  const newListItem = document.createElement("li");
  const newParagraph = document.createElement("p");
  newParagraph.innerText = message ? message : "Some error happened.";
  newListItem.appendChild(newParagraph);
  newListItem.classList.add("message", "user");
  messages.appendChild(newListItem);
  messages.scrollTop = messages.scrollHeight;
  input.value = "";

  // send message to some api
  console.log(message);
});

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

// Adds a new bot message
// const newListItemBot = document.createElement("li");
// const newImageBot = document.createElement("img");
// newImageBot.src = "./assets/Chatbot Image.webp";
// newImageBot.alt = "Avatar image for the Unibot support bot.";
// const newParagraphBot = document.createElement("p");
// newParagraphBot.innerText = "I'm lorem ipsum text!";

// newListItemBot.classList.add("message", "bot");
// newListItemBot.appendChild(newImageBot);
// newListItemBot.appendChild(newParagraphBot);
// messages.appendChild(newListItemBot);
