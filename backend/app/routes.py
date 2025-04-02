from flask import Flask, request, jsonify,flash,redirect
from flask_cors import CORS
from app import app
from reduction.PCA import resnet_PCA, vgg_PCA, inception_PCA
from reduction.tsne import resnet_tsne, vgg_tsne, inception_tsne
from werkzeug.utils import secure_filename
import torch
import torchvision.transforms.v2 as transforms
from torchvision import models
from torchvision.datasets import ImageFolder
from torchvision.models.feature_extraction import get_graph_node_names
from torchvision.models.feature_extraction import create_feature_extractor
from torch.utils.data import DataLoader
import pickle


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
    dataset_path  = 'C:/Users/16784/Desktop/server/ImageQuest/backend/test_dataset'  #Use path on local machine
    dataset = ImageFolder(root=dataset_path, transform=data_transforms)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False)

    extract = []
    for i, (image, label) in enumerate(dataloader):
        with torch.no_grad():
            output = features(image)
        extraction = output['layer4'].cpu().numpy()
        reduce = extraction.reshape(1, -1)
        extract.append(reduce)
        print(f"Image {i+1} features shape: {output['layer4'].shape}")
        
    with open('C:/Users/16784/Desktop/server/ImageQuest/backend/feature_vectors/features_resnet.pkl', 'wb') as a:
        pickle.dump(extract, a) 

    return jsonify({"message": "ResNet feature extraction"})

@app.route('/progress', methods=['GET'])
def get_progress():
    return jsonify({"progress": percent})

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

    dataset_path = 'C:/Users/16784/Desktop/server/ImageQuest/backend/test_dataset'  #Use path on local machine
    dataset = ImageFolder(root=dataset_path, transform=data_transforms)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False)

    extract = []
    for i, (image, label) in enumerate(dataloader):
        with torch.no_grad():
            output = features(image)
        extraction = output['features.28'].cpu().numpy()
        reduce = extraction.reshape(1, -1)
        extract.append(reduce)
        print(f"Image {i+1} features shape: {output['features.28'].shape}")

    with open('C:/Users/16784/Desktop/server/ImageQuest/backend/feature_vectors/features_vgg.pkl', 'wb') as b:
        pickle.dump(extract, b)

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

    dataset_path = 'C:/Users/16784/Desktop/server/ImageQuest/backend/test_dataset' #Use path on local machine
    dataset = ImageFolder(root=dataset_path, transform=data_transforms)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False)

    extract = []
    for i, (image, label) in enumerate(dataloader):
        with torch.no_grad():
            output = features(image)
        extraction = output['Mixed_7c'].cpu().numpy()
        reduce = extraction.reshape(1, -1) 
        extract.append(reduce)
        print(f"Image {i+1} features shape: {output['Mixed_7c'].shape}")

    with open('C:/Users/16784/Desktop/server/ImageQuest/backend/feature_vectors/features_inception.pkl', 'wb') as c:
        pickle.dump(extract, c)   

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






