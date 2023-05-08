import torch
import torchvision
import torchvision.transforms as transforms
from torchvision.models import resnet50
from torchvision.datasets import ImageNet
from torch.utils.data import DataLoader
from tqdm import tqdm

def get_model(model_name):
    model = torchvision.models.__dict__[model_name](pretrained=True)
    model.eval()
    return model 


def test(name, root):
    # Define the device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load the pre-trained model
    model = get_model(name)
    model.to(device)

    # Set up the ImageNet validation dataset
    val_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    val_dataset = ImageNet(root=root, split='val', transform=val_transforms)
    val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False, num_workers=4, pin_memory=True)

    # Evaluate the model on the validation set
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in tqdm(val_loader, desc="Evaluating"):
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    print(f"Accuracy on the ImageNet validation set: {accuracy:.2f}%")

def main():
    imagenet_root = ""
    for model_name in ['alexnet', 'vgg11', 'resnet18', 'resnet50', 'vgg16', 'densenet121']:
        test(model_name, imagenet_root)