import pickle
import numpy as np
from sklearn.decomposition import PCA
import firebase_admin
from firebase_admin import credentials, storage, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("imagequest-aab50-firebase-adminsdk-fbsvc-44dd473055.json")
    firebase_admin.initialize_app(cred, {"storageBucket": "imagequest-aab50.firebasestorage.app"})
bucket = storage.bucket()
def resnet_PCA():
    blob = bucket.blob('feature_vectors/resnet_features.pkl')
    file = blob.download_as_string()
    resnet_features= pickle.loads(file)
   
    pca = PCA(n_components=2)
    data_resnet = pca.fit_transform(resnet_features)

    if blob.exists():
        blob.delete()

    return data_resnet

def vgg_PCA():
    blob = bucket.blob('feature_vectors/vgg_features.pkl')
    file = blob.download_as_string()
    vgg_features= pickle.loads(file)
   
    pca = PCA(n_components=2)
    data_vgg = pca.fit_transform(vgg_features)
    
    if blob.exists():
        blob.delete()
    
    return data_vgg

def inception_PCA():
    blob = bucket.blob('feature_vectors/inception_features.pkl')
    file = blob.download_as_string()
    inception_features= pickle.loads(file)
    
    pca = PCA(n_components=2)
    data_inception = pca.fit_transform(inception_features)
    
    if blob.exists():
        blob.delete()
    
    return data_inception


