# Technical Documentation

## Approach
- Backbone: DenseNet-121 (ImageNet pretrained), final linear head = 4 classes.
- Loss: Cross-entropy; Optimizer: AdamW; Scheduler: Cosine.
- Augmentations: Horizontal flip, small rotations, normalization.

## Data Pipeline
- Dataset: COVID-19 Radiography Database (Kaggle).
- Folder-per-class; patient-level split (avoid leakage).
- Preprocessing: Resize 224×224, normalize ImageNet stats.

## Architecture & Training
- Replace classifier layer with 4-class head.
- Train for N epochs (see `configs/train.yaml`).
- Save best checkpoint to `classification_model.pth`.

## Inference
- Load weights; preprocess to 224×224; softmax for probabilities.
- Grad-CAM for visual explanation (implement full version in `src/gradcam.py`).

## Reproducibility
- All hyperparameters in `app/configs/*.yaml`.
- Python deps in `app/requirements.txt`.
