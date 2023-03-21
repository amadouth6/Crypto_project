import requests
import time
import matplotlib.pyplot as plt

url = 'http://192.168.1.253'
times = []
fig, ax = plt.subplots()

while True:
    start_time = time.time()
    response = requests.get(url, headers={'Cache-Control': 'no-cache'})
    end_time = time.time()
    
    # Vérifier le code d'état de la réponse
    if response.status_code // 100 == 2:
        elapsed_time = end_time - start_time
        times.append(elapsed_time)
        
        # Afficher le graphique
        ax.plot(times)
        plt.pause(1)