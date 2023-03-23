function sendMessage() {
    var inputField = document.querySelector(".input");
    var messageText = inputField.value;
    var chatBox = document.querySelector(".box");

    // Display user message in chat box
    var userMsg = document.createElement("div");
    userMsg.classList.add("item", "right");
    userMsg.innerHTML = '<div class="msg"><p>' + messageText + '</p></div>';
    chatBox.appendChild(userMsg);

    // TODO: Send message using AJAX or WebSocket

    // Display bot response in chat box
    var botMsg = document.createElement("div");
    botMsg.classList.add("item");
    botMsg.innerHTML = '<div class="icon"><i class="fa fa-user"></i></div><div class="msg"><p>' + getBotResponse(messageText) + '</p></div>';
    chatBox.appendChild(botMsg);

    inputField.value = "";
}
var inputField = document.querySelector(".input");
inputField.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }

function getBotResponse(message) {
    // TODO: Implement a list of queries and corresponding responses
    // Return the appropriate response based on the user's message
}
});
