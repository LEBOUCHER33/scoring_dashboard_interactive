# scoring_dashboard_interactive

## Objectif 

Développement d'un dashboard interactif pour accéder à un outil de scoring décisionnel d'octroie de crédit bancaire


## Workflow

1- configurer l'environnement de travail :
    - création d'un repo git pour le versionning du projet
    - création et activation d'un environnement virtuel
    - installer les dépendances nécessaires au projet dans le venv
    - récupérer les éléments clés pour le fonctionnement de l'api de scoring :
        - le modèle de scoring entraîné
        - les data de test pour inférer sur le modèle
        - les scripts relatifs au développement de l'api et aux tests de son fonctionnement
        - les éléments nécessaires à son deploiement sur le cloud : Dockerfile, requirements.txt
    - déployer l'api sur une solution cloud (Render)
    - tester le fonctionnement de l'api déployée via l'url publique

2- développer un dashboard interactif :
    - définir les spécifications du dashboard
    - implémenter le script Streamlit pour l'interface utilisateur
    - intégrer l'api
    - tester le dashboard en local
    - déployer sur le cloud (Render)

3- assurer CI/CD et la veille technologique

## Spécifications du dashboard

1- visualisation du profil client :
    - affichage des caractéristiques principales de la demande (montant, échéance, annuité)
    - affichage du profil client (niveau de revenus, capacité d'endettement, âge, etc)
    - graphs du profil de risque du client

2- visualisation de la prédiction :
    - visualisation du score 
    - visualisation de la probabilité associée à une barre colorimétrique d'éloignement du seuil
    - visualisation des principales features influentes sur la prédiction






