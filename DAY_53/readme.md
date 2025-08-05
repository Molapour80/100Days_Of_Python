# 📸 PhotoShare - Python Image Sharing App  

**A Flask-based web application for uploading and sharing images**  

![Demo](https://img.shields.io/badge/Demo-Live-green) 
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey)

## 🌟 Features
- **Image Uploads** (JPEG, PNG, GIF)
- **Gallery View** with responsive grid
- **SQLite Database** for image metadata
- **User-Friendly UI** with Bootstrap 5
- **Secure Filename Handling**

## 🚀 Quick Start
```bash
# 1. Clone repo
git clone https://github.com/Molapour80/100Days_of_Python.git

# 2. Setup environment (Python 3.8+ required)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run!
flask run
```

## 📂 Project Structure
```
photoshare/
├── app.py                # Main application
├── static/
│   ├── uploads/          # Image storage
│   └── styles.css        # Custom CSS
├── templates/
│   ├── base.html         # Master template
│   ├── index.html        # Gallery view
│   └── upload.html       # Upload form
└── photos.db             # Database
```
