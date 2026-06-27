importScripts(
  "https://www.gstatic.com/firebasejs/12.15.0/firebase-app-compat.js"
);

importScripts(
  "https://www.gstatic.com/firebasejs/12.15.0/firebase-messaging-compat.js"
);


firebase.initializeApp({

apiKey: "AIzaSyChfmEBP90TuAQ9sPk3swL-ZTm8GIuCycI",
authDomain: "push-notification-demo-f0cc4.firebaseapp.com",
projectId: "push-notification-demo-f0cc4",
storageBucket: "push-notification-demo-f0cc4.firebasestorage.app",
messagingSenderId: "302607376382",
appId: "1:302607376382:web:672ffe6216a3388a076aaf"

});


const messaging = firebase.messaging();


messaging.onBackgroundMessage((payload)=>{

console.log(
"Background message:",
payload
);

});
