import socket

def demarrer_serveur():
    serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 9999

    serveur_socket.bind((host, port))
    serveur_socket.listen(1)

    print(f"[*] Serveur en écoute sur {host}:{port}")

    client_socket, client_address = serveur_socket.accept()

    print(f"[+] Client connecté : {client_address}")

    while True:

        # Réception du message du client
        message_client = client_socket.recv(1024).decode('utf-8')

        if not message_client:
            break

        print(f"\nClient : {message_client}")

        if message_client.lower() == "exit":
            print("[*] Le client a quitté la discussion.")
            break

        # Réponse du serveur
        reponse = input("Serveur : ")

        client_socket.send(reponse.encode('utf-8'))

        if reponse.lower() == "exit":
            print("[*] Fermeture du serveur.")
            break

    client_socket.close()
    serveur_socket.close()

if __name__ == "__main__":
    demarrer_serveur()