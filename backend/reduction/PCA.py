import pickle
import numpy as np
from sklearn.decomposition import PCA
import firebase_admin
from firebase_admin import credentials, storage, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("imagequest-aab50-firebase-adminsdk-fbsvc-44dd473055.json")
    firebase_admin.initialize_app(cred, {"storageBucket": "imagequest-aab50.firebasestorage.app"})
bucket = storage.bucket()
db = firestore.client()
def resnet_PCA():
    blob = bucket.blob('feature_vectors/resnet_features.pkl')
    file = blob.download_as_string()
    resnet_features= pickle.loads(file)

    features_arr = []
    image_urls = []
    for x in resnet_features:
    
        features = x['features'][0]
        features_arr.append(features)
        url = x['url']
        image_urls.append(url)

    pca = PCA(n_components=2)
    data_resnet = pca.fit_transform(features_arr)

    result = []
    for i in range(len(data_resnet)):
        result.append({
        'x': data_resnet[i][0],
        'y': data_resnet[i][1],
        'image_url': image_urls[i]
    })
    
    if blob.exists():
        blob.delete()
    
    return result

def vgg_PCA():
    blob = bucket.blob('feature_vectors/vgg_features.pkl')
    file = blob.download_as_string()
    vgg_features= pickle.loads(file)
   
    features_arr = []
    image_urls = []
    for x in vgg_features:
    
        features = x['features'][0]
        features_arr.append(features)
        url = x['url']
        image_urls.append(url)

    pca = PCA(n_components=2)
    data_vgg = pca.fit_transform(features_arr)

    result = []
    for i in range(len(data_vgg)):
        result.append({
        'x': data_vgg[i][0],
        'y': data_vgg[i][1],
        'image_url': image_urls[i]
    })
    

    if blob.exists():
        blob.delete()

    return result

def inception_PCA():
    blob = bucket.blob('feature_vectors/inception_features.pkl')
    file = blob.download_as_string()
    inception_features= pickle.loads(file)
    
    features_arr = []
    image_urls = []
    for x in inception_features:
    
        features = x['features'][0]
        features_arr.append(features)
        url = x['url']
        image_urls.append(url)

    pca = PCA(n_components=2)
    data_inception = pca.fit_transform(features_arr)

    result = []
    for i in range(len(data_inception)):
        result.append({
        'x': data_inception[i][0],
        'y': data_inception[i][1],
        'image_url': image_urls[i]
    })
    


    if blob.exists():
        blob.delete()

    return result


