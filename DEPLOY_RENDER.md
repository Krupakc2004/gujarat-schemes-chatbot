# How to Deploy on Render 🚀

Render is a great free alternative for hosting Python web apps.

## Prerequisites
1.  **GitHub Account**: You need a GitHub account to host your code.
2.  **Render Account**: Sign up at [render.com](https://render.com) using your GitHub account.

## Step 1: Upload Code to GitHub
1.  Create a **New Repository** on GitHub (e.g., named `gujarat-scheme-bot`).
2.  Upload all the files from your `chatbot` folder to this repository.
    *   **Crucial Files**: `app.py`, `requirements.txt`, `Procfile`, `static/`, `templates/`.

## Step 2: Create Web Service on Render
1.  Go to your [Render Dashboard](https://dashboard.render.com/).
2.  Click the **"New +"** button and select **"Web Service"**.
3.  Select **"Build and deploy from a Git repository"**.
4.  Connect your GitHub account if you haven't already.
5.  Find your `gujarat-scheme-bot` repository and click **"Connect"**.

## Step 3: Configure Deployment
Render will ask for some details. Fill them in as follows:

*   **Name**: Give your app a unique name (e.g., `gujarat-bot-demo`).
*   **Region**: Singapore (closest to India) or Frankfurt.
*   **Branch**: `main` (or `master`).
*   **Runtime**: **Python 3**.
*   **Build Command**: `pip install -r requirements.txt`
*   **Start Command**: `gunicorn app:app`
*   **Instance Type**: **Free** (Select the Free tier).

## Step 3.1: Add Environment Variables (IMPORTANT)
1.  Click **"Advanced"** or scroll down to **"Environment Variables"**.
2.  Click **"Add Environment Variable"**.
3.  **Key**: `GEMINI_API_KEY`
4.  **Value**: Paste your actual Gemini API Key here (starting with `AIza...`).
5.  *Without this, your bot will not be able to reply.*

## Step 4: Deploy
1.  Click **"Create Web Service"**.
2.  Render will start building your app. You will see logs scrolling.
3.  Wait for a few minutes. Once it says **"Live"**, your app is deployed!
4.  Click the URL at the top (e.g., `https://gujarat-bot-demo.onrender.com`) to visit your chatbot.

## Troubleshooting
*   **"Module not found" error**: Make sure `requirements.txt` lists all libraries (`flask`, `gunicorn`).
*   **"App crashed"**: Check the "Logs" tab in Render for error messages. Ensure `Procfile` content is `web: gunicorn app:app`.
