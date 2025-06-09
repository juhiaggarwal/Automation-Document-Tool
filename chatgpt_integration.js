async function sendQuery() {
    const userQuery = document.getElementById('user-query').value;

    if (userQuery.trim() === "") {
        alert("Please enter a query.");
        return;
    }

    const assistantResponse = document.getElementById('assistant-response');

    assistantResponse.innerHTML = "Thinking...";

    // Call backend to get ChatGPT response (ensure backend handles this)
    const response = await fetch('/chatgpt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userQuery })
    });

    const data = await response.json();
    assistantResponse.innerHTML = data.reply || "Sorry, I couldn't get an answer.";
}
