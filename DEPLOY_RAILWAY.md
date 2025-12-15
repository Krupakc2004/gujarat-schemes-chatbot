# How to Deploy on Railway 🚂

## Prerequisites
1.  **GitHub Account**: You need a GitHub account to host your code.
2.  **Railway Account**: Sign up at [railway.app](https://railway.app) using your GitHub account.

## Step 1: Upload Code to GitHub
1.  Create a **New Repository** on GitHub (e.g., named `gujarat-scheme-bot`).
2.  Upload all the files from your `chatbot` folder to this repository.
    *   Ensure `app.py`, `requirements.txt`, `Procfile`, `runtime.txt`, `static/`, and `templates/` are all uploaded.

## Step 2: Deploy on Railway
1.  Go to your [Railway Dashboard](https://railway.app/dashboard).
2.  Click **"New Project"**.
3.  Select **"Deploy from GitHub repo"**.
4.  Select the repository you just created (`gujarat-scheme-bot`).
5.  Click **"Deploy Now"**.

## Step 3: Configuration (Important!)
Railway usually auto-detects everything, but let's double-check:

1.  Click on your project card.
2.  Go to the **"Settings"** tab.
3.  Scroll down to **"Networking"**.
4.  Click **"Generate Domain"**.
    *   This will give you a public URL (e.g., `gujarat-bot-production.up.railway.app`).
5.  Click on that link to see your live chatbot!

## Troubleshooting
*   **Build Failed?** Check the "Deployments" tab and click "View Logs" to see what went wrong. Usually, it's a missing library in `requirements.txt`.
*   **Application Error?** Ensure your `Procfile` is correct: `web: gunicorn app:app`.

## Note
Railway has a trial period. For permanent hosting, you might need to verify your account or upgrade later.
