# Chest X‑Ray Diagnostic Assistant 🩺

A deep learning application for analyzing chest X‑ray images, built with **PyTorch** and **Streamlit**. It provides **multi‑disease classification** and **visual localization** of potential abnormalities via **Grad‑CAM**.

> **Disclaimer:** This tool is for **education and research** only and **not** a medical device. Always consult qualified clinicians for diagnosis or treatment.

---

## 🚀 Live Application Demo
Experience the live application here:

➡️ **[Open the Live App](YOUR_STREAMLIT_URL_HERE)**  
*(Replace `YOUR_STREAMLIT_URL_HERE` with your Streamlit link.)*

---

## 📥 Required: Download the Trained Model
The trained model (`classification_model.pth`) is too large for GitHub. Download it and place it inside the `deployment/` folder **before** running the app.

➡️ **[Download the Trained Model from Google Drive](YOUR_GOOGLE_DRIVE_LINK_HERE)**  
*(Replace `YOUR_GOOGLE_DRIVE_LINK_HERE` with your actual Google Drive link.)*

**After downloading:** put `classification_model.pth` in `deployment/`

```
deployment/
├─ app.py
├─ requirements.txt
├─ utils/...
└─ classification_model.pth   ← place the file here
```

---

## ✨ Features
- **Advanced Classification:** Predicts the most likely condition among: `Normal`, `COVID`, `Lung_Opacity`, `Viral Pneumonia`.
- **Visual Localization:** Generates **Grad‑CAM** heatmaps to highlight regions contributing to predictions.
- **Interactive UI:** Clean, responsive Streamlit interface for quick testing.
- **DICOM Support:** Can read and process medical image formats (e.g., DICOM).

---

## 🧰 Tech Stack
- **Frameworks:** PyTorch, Streamlit
- **Imaging:** OpenCV / PIL, pydicom (for DICOM)
- **Explainability:** Grad‑CAM

---

## 🖥️ How to Run Locally

### 1) Clone the Repository
```bash
git clone https://github.com/azeem-aslam-ch/chest-xray-app.git
cd chest-xray-app
```

### 2) Download the Model
- Download `classification_model.pth` from the Google Drive link above.  
- Place it into the `deployment/` folder.

### 3) Install Dependencies
```bash
cd deployment
pip install -r requirements.txt
```

> Tip: Use a virtual environment (`python -m venv .venv && source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\activate` on Windows).

### 4) Launch the App
```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

---

## 📂 Repository Structure
```
chest-xray-app/
├─ deployment/
│  ├─ app.py
│  ├─ requirements.txt
│  ├─ utils/
│  └─ classification_model.pth  # (you add this)
├─ docs/
│  ├─ README_assets/ (images, diagrams)
│  └─ model_card.md
├─ notebooks/ (experiments and EDA)
└─ LICENSE
```

---

## 🧪 Usage
1. Open the app (local or Live App).  
2. Upload a chest X‑ray image (`.png`, `.jpg`, `.jpeg`, or DICOM).  
3. View the **predicted class**, **confidence**, and **Grad‑CAM heatmap**.  
4. Download results if enabled.

---

## 📝 Supported Labels
- `Normal`
- `COVID`
- `Lung_Opacity`
- `Viral Pneumonia`

*(Adjust this list if you retrain the model.)*

---

## ❗ Troubleshooting
- **Model not found:** Ensure `deployment/classification_model.pth` exists.  
- **Torch/CUDA issues:** Install CPU‑only PyTorch if you don’t have a GPU.  
- **Pillow / OpenCV errors:** Reinstall dependencies: `pip install --upgrade --force-reinstall -r requirements.txt`.  
- **DICOM import errors:** Check `pydicom` is installed and the file is valid.

---

## 🔒 Data & Privacy
All uploaded images are processed locally in your session. Do not upload personal or sensitive patient data unless you have permission and comply with applicable regulations.

---

## 📄 License
This project is released under the **MIT License** unless otherwise specified.

---

## 🙋 Contact
For issues or feature requests, open a GitHub issue or contact **Azeem Aslam**.

---

**Replace the placeholders (`YOUR_STREAMLIT_URL_HERE`, `YOUR_GOOGLE_DRIVE_LINK_HERE`) before publishing.**

