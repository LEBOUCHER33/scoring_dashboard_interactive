# image docker de base avec Python 
FROM python:3.11-slim

# repertoire de travail dans le conteneur (là où seront copiés les fichiers)
WORKDIR /app

# Installer les dépendances système utiles pour LightGBM
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# copie des dépendances 
COPY requirements.txt ./

# installation des dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copie du script lié à l'application
COPY Scripts/api.py ./Scripts/api.py

# copie du pipeline et du modèle entrainé
COPY Scripts/pipeline_final.pkl ./Scripts/pipeline_final.pkl

# expose le port local de l'api
EXPOSE 8000

# execution de l'application lors du lancement du conteneur
WORKDIR /app/Scripts
CMD ["python", "-m", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

