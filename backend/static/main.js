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
