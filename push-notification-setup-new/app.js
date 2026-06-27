import { initializeApp } from "firebase/app";
import { getMessaging, getToken } from "firebase/messaging";


// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyChfmEBP90TuAQ9sPk3swL-ZTm8GIuCycI",
  authDomain: "push-notification-demo-f0cc4.firebaseapp.com",
  projectId: "push-notification-demo-f0cc4",
  storageBucket: "push-notification-demo-f0cc4.firebasestorage.app",
  messagingSenderId: "302607376382",
  appId: "1:302607376382:web:672ffe6216a3388a076aaf"
};


// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Firebase Messaging
const messaging = getMessaging(app);


// Button click
document.getElementById("enable").addEventListener("click", async () => {

  try {

    // Request notification permission
    const permission = await Notification.requestPermission();


    if (permission === "granted") {

      console.log("Notification permission granted");


      // Register service worker
      const registration = await navigator.serviceWorker.register(
        "/firebase-messaging-sw.js",
        {
          scope: "/"
        }
      );


      console.log("Service Worker registered:", registration);


      // Wait until service worker is active
      await navigator.serviceWorker.ready;


      // Generate FCM token
      const token = await getToken(messaging, {

        vapidKey: "BNPrQKG2ZQcveLLZHRvC1G0R4L_NYrsb6vqzeStgy5qhAz_ih_RirWhC6Ae6jefqD94Uzr3DIevXxvQvwMFpGXU",

        serviceWorkerRegistration: registration

      });


      if (token) {

        console.log("FCM TOKEN:");
        console.log(token);

      } else {

        console.log("No FCM token generated");

      }


    } else {

      console.log("Notification permission denied");

    }


  } catch (error) {

    console.error("FCM Error:", error);

  }

});
