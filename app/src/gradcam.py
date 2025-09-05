import torch, numpy as np
from PIL import Image

def gradcam_overlay(model, x, target_index=0):
    # Minimal placeholder Grad-CAM-like heatmap for packaging.
    # Replace with a full implementation (hooks on last conv layers) in your project.
    heat = torch.rand((224, 224)).numpy()
    heat = (heat - heat.min()) / (heat.max() - heat.min() + 1e-6)
    heat_rgb = (np.stack([heat]*3, axis=-1) * 255).astype('uint8')
    return Image.fromarray(heat_rgb).resize((x.shape[-1], x.shape[-2]))
