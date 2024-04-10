import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Check if Firebase app has already been initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://face-recognition-94653-default-rtdb.firebaseio.com/"
    })

# Get a reference to the Firebase database
ref = db.reference('Students')

# Your data and data handling code here...


data = {}
for key, value in data.items():
    ref.child(key).set(value)
