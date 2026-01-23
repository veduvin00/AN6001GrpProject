function handleEnter(e) {
    if (e.key === "Enter") sendMessage();
}

function quickSend(text) {
    document.getElementById("userInput").value = text;
    sendMessage();
}

function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (!message) return;

    const messages = document.getElementById("messages");
    const typing = document.getElementById("typing");

    // User bubble
    const userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.innerText = message;
    messages.appendChild(userDiv);

    messages.scrollTop = messages.scrollHeight;
    input.value = "";

    typing.classList.remove("d-none");

    setTimeout(() => {
        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        })
        .then(res => res.json())
        .then(data => {
            typing.classList.add("d-none");

            const botDiv = document.createElement("div");
            botDiv.className = "bot-message";
            botDiv.innerText = data.reply;
            messages.appendChild(botDiv);

            messages.scrollTop = messages.scrollHeight;
        });
    }, 800); // bot "thinking" delay
}
