// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC2FAptGN6oZ_Gs-vjrWP7uKFFJRumrrmE",
  authDomain: "imagequest-aab50.firebaseapp.com",
  projectId: "imagequest-aab50",
  storageBucket: "imagequest-aab50.firebasestorage.app",
  messagingSenderId: "639659151457",
  appId: "1:639659151457:web:6e0c48a108d88555685a20",
  measurementId: "G-4TWKYZQPYC"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);