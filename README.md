# 🌍 GeoRiskAI

**GeoRiskAI** est une plateforme open source qui exploite l'imagerie satellite, l'intelligence artificielle et les données géospatiales pour aider les ONG à évaluer les risques environnementaux et les vulnérabilités des bâtiments, notamment dans les zones à risque ou sinistrées.

## 🎯 Objectif

Permettre aux ONG, fondations et acteurs humanitaires de :

- Identifier rapidement les zones vulnérables (toits endommagés, densité urbaine, risque d’inondation ou de feu)
- Suivre l’évolution de l’occupation des sols (urbanisation, déforestation, etc.)
- Accélérer l’évaluation post-catastrophe (séismes, inondations, incendies)
- Obtenir des analyses de risque claires et accessibles via une interface simple ou une API

Complete project setup.

## 🚀 Lancer GeoRiskAI en local

### 🧩 Prérequis

- Python 3.10+
- Node.js ≥ 18
- Docker & Docker Compose
- Compte [Copernicus SciHub](https://scihub.copernicus.eu/dhus)
- Compte **AWS S3** + droits `PutObject`

---

### 🐍 1. Installation backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Accès API : http://localhost:8000/docs

---

### 🌐 2. Installation frontend (React)

```bash
cd frontend
npm install
npm start
```

Accès interface : http://localhost:3000

---

## 🐳 Lancer avec Docker Compose (recommandé)

```bash
docker-compose up --build
```

Cela démarre :

- `backend` sur le port `8000`
- `frontend` sur le port `3000`

---

### 🔐 Configuration requise

#### Pour acces aux images Sentinel :

Dans `backend/app/utils/sentinel_downloader.py` :

```python
api = SentinelAPI("your_username", "your_password", "https://scihub.copernicus.eu/dhus")
```

#### Uploader sur AWS S3 :

Configure tes identifiants avec :

```bash
aws configure
```

Ou via variables d’environnement dans `docker-compose.yml` :

```yaml
environment:
  - AWS_ACCESS_KEY_ID=...
  - AWS_SECRET_ACCESS_KEY=...
```
