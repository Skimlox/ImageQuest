import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

#In order to run this script, you must run it with the current working directory.
def database():
    cred = credentials.Certificate("imagequest-aab50-firebase-adminsdk-fbsvc-df1a6c849d.json")
    firebase_admin.initialize_app(cred,{'storageBucket': 'imagequest-aab50.firebasestorage.app'})

    bucket = storage.bucket()
    return bucket
