# Chest X-Ray Diagnostic Assistant 🩺

A PyTorch + Streamlit app for **multi‑disease chest X‑ray classification** with **Grad‑CAM** visual explanations.  
**Disclaimer:** Research/education only — not a medical device.

---

## 🔗 Live Links
- **Live App:** https://chest-xray-app-mfawfpdbjakjdr7bsotynh.streamlit.app/
- **GitHub Repository:** https://github.com/azeem-aslam-ch/chest-xray-assignment
- **Download Trained Model (.pth):** https://drive.google.com/file/d/1JLddmWmofxj8fIjVzbu1iZlF8XQt8B2Z/view?usp=drive_link

> After downloading the model, place it at: `models/classification_model.pth` (recommended). Keep only **one** copy.

---

## 📁 Repository Structure
```
chest-xray-assignment/
├─ app/
│  ├─ .streamlit/             # Streamlit theme/config
│  ├─ configs/                # App configs (optional)
│  ├─ src/                    # UI helpers/components
│  ├─ app.py                  # Streamlit UI entry (local/dev)
│  └─ requirements.txt        # App dependencies
├─ demo/                      # Screenshots / demo assets
├─ deployment/
│  ├─ DEPLOYMENT.md           # Deployment notes
│  ├─ Dockerfile              # Docker build for production not use in this assigment 
│  ├─ Procfile                # Process entry (e.g., Render/Heroku-style) not use in this assigment 
│  └─ runtime                 # Runtime pin (e.g., python-3.x)
├─ docs/
│  ├─ APP_README.md           # End-user instructions
│  ├─ DISEASES.md             # Supported labels & notes
│  ├─ RESULTS.md              # Metrics & confusion matrix
│  └─ TECHNICAL.md            # Approach & architecture
├─ models/
│  ├─ classification_model.pth  # ← put downloaded model here (name must be same)
│  ├─ metrics.json
│  ├─ model_card.md
│  ├─ README.md
│  └─ validation_results.xlsx
├─ src/
│  └─ classification_task.py  # Training/inference utilities This is collab file 
├─ .gitattributes
├─ .gitignore
├─ LICENSE
├─ Live links.txt
└─ README.md                  # You are here
```

---

## ✨ Features
- **Classification:** `Normal`, `COVID`, `Lung_Opacity`, `Viral Pneumonia`
- **Explainability:** Grad‑CAM heatmaps
- **DICOM support:** via `pydicom`
- **Simple UI:** upload → predict → visualize

---

## 🚀 Run Locally
```bash
# 1) Clone
git clone https://github.com/azeem-aslam-ch/chest-xray-assignment.git
cd chest-xray-assignment

# 2) (Recommended) Create & activate a virtual env
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

# 3) Install dependencies
cd app
pip install -r requirements.txt

# 4) Download model and place at:
# models/classification_model.pth

# 5) Launch Streamlit
streamlit run app.py
```
Open the local URL shown in the terminal (usually `http://localhost:8501`).


---

## ☁️ Streamlit Cloud 
1. Fork/Connect the GitHub repo.  
2. Set **Main file path** to `app/app.py`.  
3. Ensure `app/requirements.txt` is detected.  
4. The model should be supplied at runtime (e.g., mounted, or downloaded in app code). If not possible, keep it locally for development.

---

## 📄 Documentation
- Quick usage: `docs/APP_README.md`  
- Diseases: `docs/DISEASES.md`  
- Results: `docs/RESULTS.md`, plus `models/metrics.json`, `models/validation_results.xlsx`  
- Technical design: `docs/TECHNICAL.md`  
- Model card: `models/model_card.md`

---

## 🧷 .gitignore (recommended)
```
# Python / temp
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
*.log

# OS
.DS_Store

# Models / artifacts
*.pth
models/
```

> Prefer hosting the model on Google Drive (link above). If you must keep it in the repo, use **Git LFS**:
> ```bash
> git lfs install
> git lfs track "*.pth"
> git add .gitattributes
> git commit -m "Track model files with LFS"
> git push
> ```

---

## ❗ Troubleshooting
- **Model not found:** ensure `models/classification_model.pth` exists at runtime.  
- **CUDA issues:** use CPU build of PyTorch if no GPU is available.  
- **DICOM read errors:** verify `pydicom` is installed and file is valid.  
- **Port blocked:** change `-p 8501:8501` to another port, e.g., `-p 8502:8501`.

---

## 📜 License
See `LICENSE`.

## 👤 Contact
**Azeem Aslam** — open an issue on GitHub or use the contacts in *Live links.txt*.
Mobile: +923324308550
www.azeemaslam.com
