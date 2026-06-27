# 🔔 Firebase Push Notification Setup (FCM)

A web-based push notification system using *Firebase Cloud Messaging (FCM)* to deliver real-time browser notifications even when the application is not actively open.

## 🚀 Features

- Firebase Cloud Messaging integration
- Browser notification permission handling
- FCM token generation
- Service Worker support
- Push notification sending using Firebase Admin SDK

## 🛠️ Tech Stack

- JavaScript
- Node.js
- Vite
- Firebase Web SDK
- Firebase Admin SDK

## 📂 Project Structure


push-notification-setup/
│
├── index.html
├── app.js
├── firebase-messaging-sw.js
├── send.cjs
├── package.json
└── README.md


## ⚙️ Setup

Install dependencies:

bash
npm install


Run project:

bash
npm run dev


Open the localhost URL, allow notifications, and generate the FCM token.

## 📩 Send Notification

Run:

bash
node send.cjs


Successful response:

json
{
  "fcm_status": "success",
  "message_id": "projects/xxx/messages/yyy"
}


## 🔐 Security

Sensitive files like:


serviceAccountKey.json
node_modules/


are excluded using .gitignore.

## 👩‍💻 Author

Gungun Jain
