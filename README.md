# Gujarat Government Complaint Chatbot

This is a Flask-based chatbot for registering complaints for Gujarat Government departments.

## Prerequisites

- Python 3.x
- Flask

## Installation

1.  Install Flask if you haven't already:
    ```bash
    pip install flask
    ```

## Running the Application

1.  Navigate to the project directory:
    ```bash
    cd c:/Users/Ideapad slim3/Desktop/chatbot
    ```

2.  Run the Flask application:
    ```bash
    python app.py
    ```

3.  Open your web browser and go to:
    ```
    http://127.0.0.1:5000
    ```

## Usage

1.  Click the chat icon at the bottom-right corner.
2.  Start chatting! You can use English or Gujarati.
3.  Follow the bot's prompts to register a complaint.

## Features

-   **Language Detection**: Automatically detects English or Gujarati.
-   **Validation**: Validates mobile numbers (10 digits) and ensures descriptions are not empty.
-   **State Management**: Guides the user through a structured flow.
