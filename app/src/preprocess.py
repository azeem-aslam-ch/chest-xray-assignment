from torchvision import transforms

# Basic preprocessing; align with training pipeline
def get_transform():
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

def to_tensor(pil_img):
    t = get_transform()
    return t(pil_img)
