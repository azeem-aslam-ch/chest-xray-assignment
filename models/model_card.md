# Model Card — DenseNet-121 (Chest X-Ray, 4-class)

## Overview
Multi-class classifier trained on COVID-19 Radiography Database (Kaggle). Targets:
**Normal, COVID, Lung Opacity, Viral Pneumonia**.

## Intended Use & Users
- Educational/testing. **Not** for clinical diagnosis.
- For demo of classification + Grad-CAM.

## Training Data
- COVID-19 Radiography Database (Kaggle). Follow dataset license.

## Metrics (fill with your results)
--- Average Precision (AP) for Each Class ---
Normal: 0.9864
COVID: 0.9997
Lung_Opacity: 0.9804
Viral Pneumonia: 0.9984

==================================================
Mean Average Precision (mAP): 0.9912
==================================================
## Evaluation Protocol
- Train/val split with patient-level separation.

## Limitations
- Dataset biases/quality.
- Domain shift vs. real-world hospital data.
- Not a medical device.

## Ethical Considerations & Risks
- Misclassification risk; must not be used for clinical decisions.
- Potential demographic performance disparities.

## Contact
Author: Azeem Aslam
Live demo: https://chest-xray-app-mfawfpdbjakjdr7bsotynh.streamlit.app/
