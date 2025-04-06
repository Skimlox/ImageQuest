import os
from flask import Flask, request, jsonify,flash,redirect
from flask_cors import CORS
from app import app
import requests
from reduction.PCA import resnet_PCA, vgg_PCA, inception_PCA
from reduction.tsne import resnet_tsne, vgg_tsne, inception_tsne
from werkzeug.utils import secure_filename
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import tempfile
import torch
import torchvision.transforms.v2 as transforms
from torchvision import models
from torchvision.datasets import ImageFolder
from torchvision.models.feature_extraction import get_graph_node_names
from torchvision.models.feature_extraction import create_feature_extractor
from torch.utils.data import DataLoader
import pickle
import firebase_admin
from firebase_admin import credentials, firestore,storage
import numpy as np

cred = credentials.Certificate("imagequest-aab50-firebase-adminsdk-fbsvc-44dd473055.json")
firebase_admin.initialize_app(cred,{"storageBucket": "imagequest-aab50.firebasestorage.app"})
db = firestore.client()
bucket = storage.bucket()

@app.route('/resnet', methods=['POST'])
def resnet_NN():
    model =  models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
    model.eval()

    data_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToImage(), 
        transforms.ToDtype(torch.float32, scale=True),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])

    return_nodes = {
    'layer4': 'layer4',
}
    features =  create_feature_extractor(model, return_nodes=return_nodes)
    collection = db.collection('main2').stream(timeout=300)

    extract = []
    for x in collection:
        image = x.to_dict()
        image_url = image['url']
        image_id = image['image_id']
        try:
            get_image = requests.get(image_url, timeout=300)
            if get_image.status_code != 200:
                print("CANNOT GET IMAGE")
                continue

            read_image = Image.open(BytesIO(get_image.content)).convert('RGB')
            image_transform = data_transforms(read_image).unsqueeze(0)

            with torch.no_grad():
                output = features(image_transform)

            extraction = output['layer4'].cpu().numpy()
            reduce = extraction.reshape(1, -1)
            extract.append(reduce)

            print(f"FEATURES EXTRACTED: {image_id}: {reduce.shape}")
        except UnidentifiedImageError:
            print("UNIDENTIFIED IMAGE ERROR")
        except Exception as e:
            print("ERROR")
    stack_list = np.vstack(extract)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.pkl') as temp_file:
        pickle.dump(stack_list, temp_file)
        temp_filename = temp_file.name 
    blob = bucket.blob("feature_vectors/resnet_features.pkl")
    blob.upload_from_filename(temp_filename)
    os.remove(temp_filename) 

    return jsonify({"message": "ResNet feature extraction"})

@app.route('/vgg', methods=['POST'])
def vgg_NN():
    model = models.vgg16(weights=models.VGG16_Weights.DEFAULT)
    model.eval()


    data_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToImage(), 
    transforms.ToDtype(torch.float32, scale=True),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])


    return_nodes = {
    'features.28': 'features.28', 
}
    features = create_feature_extractor(model, return_nodes=return_nodes)
    collection = db.collection('main2').stream(timeout=300)

    extract = []
    for x in collection:
        image = x.to_dict()
        image_url = image['url']
        image_id = image['image_id']
        try:
            get_image = requests.get(image_url, timeout=300)
            if get_image.status_code != 200:
                print("CANNOT GET IMAGE")
                continue
            read_image = Image.open(BytesIO(get_image.content)).convert('RGB')
            image_transform = data_transforms(read_image).unsqueeze(0)

            with torch.no_grad():
                output = features(image_transform)

            extraction = output['features.28'].cpu().numpy()
            reduce = extraction.reshape(1, -1)
            extract.append(reduce)

            print(f"FEATURES EXTRACTED: {image_id}: {reduce.shape}")
        except UnidentifiedImageError:
            print("UNIDENTIFIED IMAGE ERROR")
        except Exception as e:
            print("ERROR")
    stack_list = np.vstack(extract)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.pkl') as temp_file:
        pickle.dump(stack_list, temp_file)
        temp_filename = temp_file.name 
    blob = bucket.blob("feature_vectors/vgg_features.pkl")
    blob.upload_from_filename(temp_filename)
    os.remove(temp_filename)

    return jsonify({"message": "VGG feature extraction"})


@app.route('/inception', methods=['POST'])
def inception_NN():
    model = models.inception_v3(weights=models.Inception_V3_Weights.DEFAULT)
    model.eval()


    data_transforms = transforms.Compose([
    transforms.Resize(299),
    transforms.CenterCrop(299),  
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]), 
])


    return_nodes = {
    'Mixed_7c': 'Mixed_7c',  
}

    features = create_feature_extractor(model, return_nodes=return_nodes)
    collection = db.collection('main2').stream(timeout=300)

    extract = []
    for x in collection:
        image = x.to_dict()
        image_url = image['url']
        image_id = image['image_id']
        try:
            get_image = requests.get(image_url, timeout=300)
            if get_image.status_code != 200:
                print("CANNOT GET IMAGE")
                continue

            read_image = Image.open(BytesIO(get_image.content)).convert('RGB')
            image_transform = data_transforms(read_image).unsqueeze(0)

            with torch.no_grad():
                output = features(image_transform)

            extraction = output['Mixed_7c'].cpu().numpy()
            reduce = extraction.reshape(1, -1)
            extract.append(reduce)

            print(f"FEATURES EXTRACTED: {image_id}: {reduce.shape}")
        except UnidentifiedImageError:
            print("UNIDENTIFIED IMAGE ERROR")
        except Exception as e:
            print("ERROR")
    stack_list = np.vstack(extract)


    with tempfile.NamedTemporaryFile(delete=False, suffix='.pkl') as temp_file:
        pickle.dump(stack_list, temp_file)
        temp_filename = temp_file.name 
    blob = bucket.blob("feature_vectors/inception_features.pkl")
    blob.upload_from_filename(temp_filename)
    os.remove(temp_filename) 

    return jsonify({"message": "Inception feature extraction"})

@app.route('/resnetpca', methods=['POST'])
def resnetpca():
    coordinates = resnet_PCA()
    return jsonify(coordinates.tolist())

@app.route('/vggpca', methods=['POST'])
def vggpca():
    coordinates = vgg_PCA()
    return jsonify(coordinates.tolist())

@app.route('/inceptionpca', methods=['POST'])
def inceptionpca():
    coordinates = inception_PCA()
    return jsonify(coordinates.tolist())


@app.route('/resnettsne', methods=['POST'])
def resnettsne():
    coordinates = resnet_tsne()
    return jsonify(coordinates.tolist())

@app.route('/vggtsne', methods=['POST'])
def vggtsne():
    coordinates = vgg_tsne()
    return jsonify(coordinates.tolist())

@app.route('/inceptiontsne', methods=['POST'])
def inceptiontsne():
    coordinates = inception_tsne()
    return jsonify(coordinates.tolist())






