📌 Backend Assignment - Django Application

1️⃣ Project Overview

This Django-based backend application includes:

Google OAuth 2.0 Authentication

Google Drive Integration (Upload, List, Download Files)

WebSocket for Real-Time Chat (Tested using wscat, supports raw text messages)

🚀 Live API URL: https://backend-assignment-qycp.onrender.com/

2️⃣ How to Clone the Project and Push to Your Own GitHub Repository

Follow these steps to download the existing project locally and then push it to your own GitHub repository.

🔹 Step 1: Download the Project Locally

git clone https://github.com/purvangshah2608/backend-assignment.git
cd backend-assignment

🔹 Step 2: Replace client_secret.json with Your Own Credentials

IMPORTANT: The project contains my client_secret.json, which will NOT work on your own hosted version.You must replace it with your own credentials (instructions in the next section).

rm client_secret.json

Follow the instructions below to generate your own Google OAuth client_secret.json.

Move your newly downloaded client_secret.json into the project directory.

🔹 Step 3: Push the Project to a New GitHub Repository

Create a new GitHub repository:

Go to GitHub.

Click "New Repository".

Name it backend-assignment.

Do NOT initialize with README, .gitignore, or LICENSE.

Push the local project to the new GitHub repository:

git remote remove origin  # Remove the existing remote (if any)
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/backend-assignment.git
git branch -M main
git push -u origin main

3️⃣ How to Set Up Google OAuth 2.0 and Google Drive API

Since this project uses Google OAuth 2.0 and Google Drive API, you need to set up your own credentials before deploying it.

🔹 Step 1: Create a Google Cloud Project

Go to Google Cloud Console.

Click "Select a project" → "New Project".

Name your project (e.g., backend-assignment) and click "Create".

🔹 Step 2: Enable OAuth 2.0 & Google Drive API

Select your project in Google Cloud Console.

Go to APIs & Services → Enabled APIs & Services.

Click "Enable APIs & Services" and search for:

OAuth 2.0 API → Click Enable

Google Drive API → Click Enable

🔹 Step 3: Create OAuth 2.0 Credentials

Go to APIs & Services → Credentials.

Click "Create Credentials" → "OAuth client ID".

Select Application Type: Web Application.

Under Authorized Redirect URIs, add:

https://backend-assignment-qycp.onrender.com/auth/callback/

Click "Create" and download the client_secret.json file.

🔹 Step 4: Replace client_secret.json in Your Project

rm client_secret.json
mv /path/to/downloaded/client_secret.json .

Then commit and push the updated file:

git add client_secret.json
git commit -m "Replaced client_secret.json with my own credentials"
git push origin main

4️⃣ How to Deploy and Run on Render

This application is hosted on Render. Follow these steps to deploy it.

🔹 Step 1: Deploy on Render

Go to Render.

Click "New Web Service".

Select "Connect a GitHub Repository" and choose your backend-assignment repo.

🔹 Step 2: Set Deployment Commands

✅ Build Command

pip install -r requirements.txt && python manage.py migrate

✅ Start Command

daphne -b 0.0.0.0 -p $PORT backend_assignment.asgi:application

🔹 Step 3: Set Environment Variables

Go to Render → Settings → Environment Variables, then add:

GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=https://backend-assignment-qycp.onrender.com/auth/callback/

🔹 Step 4: Deploy the Application

Click "Deploy Web Service".

Wait for Render to build and deploy the application.

Visit your Render URL:

https://backend-assignment-qycp.onrender.com/

🎉 Your Django application is now live!

5️⃣ How to Test Each API Endpoint

All API endpoints can be tested using Postman.

📌 Download the Postman Collection:👉 Backend Assignment APIs.postman_collection.json

✅ Google OAuth Endpoints

Get Google Auth URL

Method: GET

URL:

https://backend-assignment-qycp.onrender.com/auth/login/

✅ Google Drive Endpoints

Upload a File

Method: POST

Headers: Authorization: Bearer your-google-auth-token

Body: file (form-data)

URL:

https://backend-assignment-qycp.onrender.com/drive/upload/

List Files

Method: GET

Headers: Authorization: Bearer your-google-auth-token

URL:

https://backend-assignment-qycp.onrender.com/drive/files/

Download a File

Method: GET

Headers: Authorization: Bearer your-google-auth-token

URL:

https://backend-assignment-qycp.onrender.com/drive/download/?file_id=YOUR_FILE_ID

✅ WebSocket Real-Time Chat (Using Raw Text)

Install wscat:

npm install -g wscat

Open two terminals and connect:

wscat -c wss://backend-assignment-qycp.onrender.com/ws/chat/

Send a raw text message:

Hello, how are you?

Receive the message in the other terminal instantly.

6️⃣ Video Demo

🎥 Watch the full walkthrough:👉 https://youtu.be/vmJ-FJk3CLU
