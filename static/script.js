document.addEventListener('DOMContentLoaded', () => {
    const chatIcon = document.getElementById('chatIcon');
    const chatWindow = document.getElementById('chatWindow');
    const closeBtn = document.getElementById('closeBtn');
    const sendBtn = document.getElementById('sendBtn');
    const userInput = document.getElementById('userInput');
    const chatBody = document.getElementById('chatBody');

    // Toggle Chat Window
    chatIcon.addEventListener('click', () => {
        chatWindow.style.display = 'flex';
        chatIcon.style.display = 'none';
        userInput.focus();
    });

    closeBtn.addEventListener('click', () => {
        chatWindow.style.display = 'none';
        chatIcon.style.display = 'flex';
    });

    // Send Message
    function sendMessage() {
        const message = userInput.value.trim();
        if (message === '') return;

        // Add User Message
        addMessage(message, 'user-message');
        userInput.value = '';

        // Show typing indicator (optional, skipped for simplicity)

        // Send to Backend
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
            .then(response => response.json())
            .then(data => {
                addMessage(data.response, 'bot-message');
            })
            .catch(error => {
                console.error('Error:', error);
                addMessage("Sorry, something went wrong. Please try again.", 'bot-message');
            });
    }

    sendBtn.addEventListener('click', sendMessage);

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function addMessage(text, className) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', className);
        messageDiv.textContent = text;
        chatBody.appendChild(messageDiv);
        scrollToBottom();
    }

    function scrollToBottom() {
        chatBody.scrollTop = chatBody.scrollHeight;
    }
});
