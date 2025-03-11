import torch
import torchvision.models as models

# Function to load the selected model
def get_feature_extractor(model_name):
    if model_name == "resnet50":
        model = models.resnet50(pretrained=True)
        model = torch.nn.Sequential(*list(model.children())[:-1])  # Remove classification layer
    elif model_name == "vgg16":
        model = models.vgg16(pretrained=True)
        model = torch.nn.Sequential(*list(model.children())[:-1])  
    elif model_name == "efficientnet_b0":
        model = models.efficientnet_b0(pretrained=True)
        model = torch.nn.Sequential(*list(model.children())[:-1])
    else:
        raise ValueError("Unsupported model")

    model.eval()  # Set to evaluation mode
    return model

# Example usage
selected_model = get_feature_extractor("resnet50")
