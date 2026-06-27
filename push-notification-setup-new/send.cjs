const { initializeApp, cert } = require("firebase-admin/app");
const { getMessaging } = require("firebase-admin/messaging");

const serviceAccount = require("./serviceAccountKey.json");

initializeApp({
  credential: cert(serviceAccount)
});

const token = "dP1IkySIE7HEMiFBzv9sQb:APA91bFAKyMq_i5G3ySj5j08Zf6Hlr9VWF484lEt4DR7TfHzUjBpnOGVGWi9nTYPVIGCzH_7aJa8dtFui-aAZ42h3nc_jjjfFc-tbdmnOGJv2-uyyz7EkGM";

const message = {
  token: token,
  notification: {
    title: "Test Notification",
    body: "Hello from Firebase"
  }
};

getMessaging()
  .send(message)
  .then((response) => {
    console.log("SUCCESS:", response);
  })
  .catch((error) => {
    console.log("ERROR:", error);
  });
