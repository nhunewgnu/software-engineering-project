document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("chat-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const input = document.getElementById("chat-input");
    const message = input.value.trim();

    if (message.length > 0) {
      const xhr = new XMLHttpRequest();

      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          const answer = response.answer;
          displayMessage(message, "right");
          displayMessage(answer, "left");
          input.value = "";
        }
      };

      xhr.open("POST", "http://127.0.0.1:5000/ask", true);
      xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
      xhr.send(JSON.stringify({ message: message }));
    }
  });
});

function displayMessage(message, alignment) {
  const box = document.querySelector(".box");
  const item = document.createElement("div");
  const icon = document.createElement("div");
  const msg = document.createElement("div");
  const p = document.createElement("p");

  item.className = `item ${alignment}`;
  icon.className = "icon";
  msg.className = "msg";
  p.textContent = message;

  msg.appendChild(p);
  item.appendChild(icon);
  item.appendChild(msg);
  box.appendChild(item);
}
