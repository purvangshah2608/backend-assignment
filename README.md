📌 Backend Assignment - Django Application

1️⃣ Project Overview

This Django-based backend application includes:

Google OAuth 2.0 Authentication

Google Drive Integration (Upload, List, Download Files)

WebSocket for Real-Time Chat (Tested using wscat)

🚀 Live API URL: https://backend-assignment-qycp.onrender.com/

2️⃣ How to Clone the Project and Push to Your Own GitHub Repository

Follow these steps to download the existing project locally and then push it to your own GitHub repository.

🔹 Step 1: Download the Project Locally

Open a terminal and run:

git clone https://github.com/YOUR_USERNAME/backend-assignment.git

(Replace YOUR_USERNAME with the actual GitHub username from where you are downloading the repo.)

Navigate to the project directory:

cd backend-assignment

🔹 Step 2: Replace client_secret.json with Your Own Credentials

IMPORTANT: The project you cloned contains my client_secret.json, which will NOT work if you are deploying your own version. You must replace it with your own credentials.

Delete the existing client_secret.json from your cloned project:

rm client_secret.json

Follow the instructions below to generate your own client_secret.json.

Move your newly downloaded client_secret.json into the project directory.

🔹 Step 3: Push the Project to a New GitHub Repository

Create a new GitHub repository:

Go to GitHub

Click New Repository.

Name it backend-assignment.

Do NOT initialize with README, .gitignore, or LICENSE.

Push the local project to the new GitHub repository:

git remote remove origin  # Remove the existing remote (if any)
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/backend-assignment.git
git branch -M main
git push -u origin main

🚨 Handling GitHub Push Errors (Secret Scanning Blocks)

When pushing the project to GitHub, you may encounter an error similar to this:

remote:        (?) To push, remove secret from commit(s) or follow this URL to allow the secret.
remote:        https://github.com/YOUR_GITHUB_USERNAME/backend-assignment/security/secret-scanning/unblock-secret/2uD4bg0RxyZPgnEJdpv8BbTrwaJ
remote:     
remote:       —— Google OAuth Client Secret ————————————————————————

🔹 Fix: Allow the Push for Testing Purposes

Copy the URL from the error message (e.g. https://github.com/YOUR_GITHUB_USERNAME/backend-assignment/security/secret-scanning/unblock-secret/...).

Paste the URL in your browser and open it.

Select "Used for test" and confirm to bypass GitHub’s secret scanning.

Retry pushing the code:

git push origin main

🚀 Now, your project is successfully pushed to your own GitHub repository!

3️⃣ How to Set Up Google OAuth 2.0 and Google Drive API

Since this project uses Google OAuth 2.0 and Google Drive API, you need to set up your own credentials before deploying it.

🔹 Step 1: Create a Google Cloud Project

Go to Google Cloud Console.

Click Select a project → New Project.

Name your project (e.g., backend-assignment) and click Create.

🔹 Step 2: Enable OAuth 2.0 & Google Drive API

In Google Cloud Console, select your project.

Go to APIs & Services → Enabled APIs & Services.

Click Enable APIs & Services and search for:

OAuth 2.0 API → Click Enable

Google Drive API → Click Enable

🔹 Step 3: Create OAuth 2.0 Credentials

In Google Cloud Console, go to APIs & Services → Credentials.

Click Create Credentials → OAuth client ID.

Select Application Type → Web Application.

Under Authorized Redirect URIs, add:

https://backend-assignment-qycp.onrender.com/auth/callback/

Click Create and download the client_secret.json file.

🔹 Step 4: Replace client_secret.json in Your Project

IMPORTANT: If you do not replace this file, authentication will not work on your own hosted deployment.

Delete the existing client_secret.json from the cloned project:

rm client_secret.json

Move your newly downloaded client_secret.json into the project directory.

Commit and push the updated file to your GitHub repository:

git add client_secret.json
git commit -m "Replaced client_secret.json with my own credentials"
git push origin main

4️⃣ How to Deploy and Run on Render

Follow the instructions to deploy the API on Render.

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

Go to Render → Settings → Environment Variables.

Add the following key-value pairs:

GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=https://backend-assignment-qycp.onrender.com/auth/callback/
DEBUG=False
DJANGO_ALLOWED_HOSTS=backend-assignment-qycp.onrender.com

🔹 Step 4: Deploy the Application

Click "Deploy Web Service".

Wait for Render to build and deploy the application.

After deployment is successful, visit your Render URL:

https://backend-assignment-qycp.onrender.com/

🎉 Your Django application is now live!

5️⃣ Postman Collection

📌 Download the Postman Collection: https://github.com/purvangshah2608/backend-assignment/blob/main/Backend%20Assignment%20APIs.postman_collection.json

6️⃣ Video Demo

🎥 Watch the full walkthrough: YouTube Link
