import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage,firestore

#In order to run this script, you must run it with the current working directory.
def database():
    if not firebase_admin._apps:
        cred = credentials.Certificate("imagequest-aab50-firebase-adminsdk-fbsvc-44dd473055.json")
        firebase_admin.initialize_app(cred, {"storageBucket": "imagequest-aab50.firebasestorage.app"})
    db = firestore.client()
    bucket = storage.bucket()
    blobs = bucket.list_blobs(prefix='chess_dataset2/')
    for x in blobs:
        url = f"https://storage.googleapis.com/{bucket.name}/{x.name}"
        doc_ref = db.collection('main2').document()
        doc_ref.set({
            'image_id': x.name,
            'url': url
        })
        print("URL ADDED!")
database()

