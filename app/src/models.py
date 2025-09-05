import torch
import torch.nn as nn
from torchvision.models import densenet121

def get_model(num_classes=4):
    m = densenet121(weights='IMAGENET1K_V1')
    in_feats = m.classifier.in_features
    m.classifier = nn.Linear(in_feats, num_classes)
    return m
