import io, os, pathlib, tempfile, torch
from PIL import Image
import numpy as np

from .models import get_model
from .preprocess import to_tensor
from .gradcam import gradcam_overlay

CLASS_NAMES = ['Normal', 'COVID', 'Lung Opacity', 'Viral Pneumonia']

def _weights_path():
    # Try root first, then models/
    for candidate in ["classification_model.pth", os.path.join("models","classification_model.pth")]:
        if os.path.exists(candidate):
            return candidate
    return None

def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = get_model(num_classes=len(CLASS_NAMES))
    wp = _weights_path()
    if wp and os.path.getsize(wp) > 0:
        state = torch.load(wp, map_location=device)
        model.load_state_dict(state)
    model.eval().to(device)
    return model, device, CLASS_NAMES

@torch.inference_mode()
def predict_with_gradcam(file, model, device, class_names):
    img = Image.open(file).convert("RGB")
    x = to_tensor(img).to(device)
    logits = model(x.unsqueeze(0))
    probs = torch.softmax(logits, dim=1).squeeze(0).cpu().numpy()

    overlay = gradcam_overlay(model, x.to(device), target_index=int(np.argmax(probs)))

    return {
        "input_image": img,
        "overlay": overlay,
        "probs": probs.tolist(),
        "pred_class": class_names[int(np.argmax(probs))]
    }
