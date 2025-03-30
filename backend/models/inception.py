import torch
import torchvision.transforms as transforms
from torchvision import models
from torchvision.datasets import ImageFolder
from torchvision.models.feature_extraction import get_graph_node_names
from torchvision.models.feature_extraction import create_feature_extractor
from torch.utils.data import DataLoader
import pickle

model = models.inception_v3(weights=models.Inception_V3_Weights.DEFAULT)
model.eval()

train_nodes, eval_nodes = get_graph_node_names(model)
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

dataset_path = 'C:/Users/16784/Desktop/server/ImageQuest/backend/test_dataset'
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