# 🖼️ Picture Management API (Python + Flask)

This is a backend REST API service for managing a collection of pictures. It supports CRUD operations and returns JSON responses. Built using **Python** and **Flask**, this project was developed as part of a back-end development course and is ready for containerized deployment using Docker.

---

## 🧰 Tech Stack

- **Language**: Python 3.x
- **Framework**: Flask (micro-framework for web services)
- **Data Store**: Local JSON file (`pictures.json`)
- **Containerization**: Docker
- **Testing**: pytest

---

## 📦 Features

- `GET /health` - Health check endpoint  
- `GET /count` - Returns the total number of pictures  
- `GET /pictures` - Returns a list of all pictures  
- `GET /pictures/<id>` - Returns a specific picture by ID  
- `POST /pictures` - Adds a new picture  
- `PUT /pictures/<id>` - Updates an existing picture  
- `DELETE /pictures/<id>` - Deletes a picture  

---

## 🚀 Getting Started

### Clone and Run Locally

```bash
git clone https://github.com/Silvafox76/back-end-picture-api.git
cd back-end-picture-api
pip install -r requirements.txt
python app.py
The server will start on http://localhost:5000.

🐳 Run with Docker
bash
Copy
Edit
docker build -t picture-api .
docker run -p 5000:5000 picture-api

.
├── backend/
│   └── routes.py          # API route logic
│   └── pictures.json      # Picture data store
├── tests/                 # pytest-based test suite
├── Dockerfile             # Container configuration
├── app.py                 # Entry point
├── requirements.txt       # Python dependencies
└── README.md              # This file
