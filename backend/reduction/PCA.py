import pickle
import numpy as np
from sklearn.decomposition import PCA
from app import __init_db__


def resnet_PCA():
    with open('C:/Users/16784/Desktop/server/ImageQuest/backend/feature_vectors/features_resnet.pkl', 'rb') as a:
        feature_vectors_resnet = pickle.load(a)
    # pickled data has been serialized so it can be stored as a byte stream
    # pickle.load unserializes it so it can be read as python code once again

    # np.vstack takes a sequence of arrays, and returns a singular array that contains all of the sequenced arrays
    num_resnet = np.vstack(feature_vectors_resnet)

    
    # uses PCA method to reduce the long array into plot points
    pca = PCA(n_components=2)
    data_resnet = pca.fit_transform(num_resnet)
    
    
    ### populate the database table of DatasetVectors, with the vstack
    ### or use this method whereever the data_resnet is returned to?
    # __init_db__.populate_DatasetVectors(data_resnet)
    
    return data_resnet

def vgg_PCA():
    with open('C:/Users/16784/Desktop/server/ImageQuest/backend/feature_vectors/features_vgg.pkl', 'rb') as b:
        feature_vectors_vgg = pickle.load(b)
    num_vgg = np.vstack(feature_vectors_vgg)

    pca = PCA(n_components=2)
    data_vgg = pca.fit_transform(num_vgg)

    return data_vgg

def inception_PCA():
    with open('C:/Users/16784/Desktop/server/ImageQuest/backend/feature_vectors/features_vgg.pkl', 'rb') as c:
        feature_vectors_inception = pickle.load(c)
    num_inception = np.vstack(feature_vectors_inception)

    pca = PCA(n_components=2)
    data_inception = pca.fit_transform(num_inception)

    return data_inception


