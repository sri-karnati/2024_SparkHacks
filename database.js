const { initializeApp } = require('firebase/app');

const admin = require("firebase-admin");

const serviceAccount = require("/Users/abhineti/Desktop/2024_SparkHacks/hackathon-6fcbc-firebase-adminsdk-a0gns-fe66ea593e.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://hackathon-6fcbc-default-rtdb.firebaseio.com"
});

function writeUserData(userId, name, email, imageUrl) {
    const db = admin.database();
    db.ref('users/' + userId).set({
        username: name,
        email: email,
        profile_picture: imageUrl
    });
}

// Example usage
writeUserData("userID123", "John Doe", "john@example.com", "https://example.com/profile.jpg");

