# Chatbot PyQt5

Ce projet est une application de chatbot développée en utilisant PyQt5. L'application permet à l'utilisateur d'interagir avec un modèle d'IA via une interface graphique. L'utilisateur peut envoyer des messages à l'IA et recevoir des réponses en temps réel.

## Caractéristiques

- Interface graphique
- Les messages de l'utilisateur et les réponses de l'IA sont affichés dans l'historique des messages.
- Les messages sont envoyés en appuyant sur la touche Entrée ou en cliquant sur le bouton "Envoyer".
- L'historique des messages est en lecture seule pour l'utilisateur.

## Dépendances

- PyQt5 pour l'interface graphique.
- requests pour envoyer des requêtes HTTP à l'API de l'IA.
- jsonlines pour lire les réponses de l'API de l'IA.

## Utilisation

Définir l'url, le port et le modèle du serveur Ollama.
``` python
url = "http://url:port/api/generate"
"model": "your-model-name",
```


Pour exécuter l'application, utilisez la commande suivante :

```bash
python3 app.py
```
