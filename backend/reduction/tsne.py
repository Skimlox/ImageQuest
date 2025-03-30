import pickle
import numpy as np
from sklearn.manifold import TSNE

def resnet_tsne():
    with open('C:/Users/16784/Desktop/server/ImageQuest/backend/feature_vectors/features_resnet.pkl', 'rb') as a:
        feature_vectors_resnet = pickle.load(a)
    num_resnet = np.vstack(feature_vectors_resnet)

    tsne = TSNE(n_components=2)
    data_resnet = tsne.fit_transform(num_resnet)
    
    return data_resnet

def vgg_tsne():
    with open('C:/Users/16784/Desktop/server/ImageQuest/backend/feature_vectors/features_vgg.pkl', 'rb') as b:
        feature_vectors_vgg = pickle.load(b)
    num_vgg = np.vstack(feature_vectors_vgg)

    tsne = TSNE(n_components=2)
    data_vgg = tsne.fit_transform(num_vgg)

    return data_vgg

def inception_tsne():
    with open('C:/Users/16784/Desktop/server/ImageQuest/backend/feature_vectors/features_vgg.pkl', 'rb') as c:
        feature_vectors_inception = pickle.load(c)
    num_inception = np.vstack(feature_vectors_inception)

    tsne = TSNE(n_components=2)
    data_inception = tsne.fit_transform(num_inception)

    return data_inception