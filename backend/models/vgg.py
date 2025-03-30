import torch
import torchvision.transforms.v2 as transforms
from torchvision import models
from torchvision.datasets import ImageFolder
from torchvision.models.feature_extraction import get_graph_node_names
from torchvision.models.feature_extraction import create_feature_extractor
from torch.utils.data import DataLoader
import pickle

model = models.vgg16(weights=models.VGG16_Weights.DEFAULT)
model.eval()

train_nodes, eval_nodes = get_graph_node_names(model)


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

dataset_path = 'C:/Users/16784/Desktop/server/ImageQuest/backend/test_dataset'
dataset = ImageFolder(root=dataset_path, transform=data_transforms)
dataloader = DataLoader(dataset, batch_size=1, shuffle=False)

extract = []
for i, (image, label) in enumerate(dataloader):
    with torch.no_grad():
        output = features(image)
    extraction = output['features.28'].cpu().numpy().flatten()
    extract.append(extraction)
    print(f"Image {i+1} features shape: {output['features.28'].shape}")

with open('C:/Users/16784/Desktop/server/ImageQuest/backend/feature_vectors/features_vgg.pkl', 'wb') as b:
    pickle.dump(extract, b)