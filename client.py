import socket

def demarrer_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 9999

    try:
        client_socket.connect((host, port))

        print("[+] Connecté au serveur")

        while True:

            # Saisie du message
            message = input("Client : ")

            client_socket.send(message.encode('utf-8'))

            if message.lower() == "exit":
                print("[*] Fermeture du client.")
                break

            # Réception de la réponse
            reponse = client_socket.recv(1024).decode('utf-8')

            print(f"\nServeur : {reponse}")

            if reponse.lower() == "exit":
                print("[*] Le serveur a quitté la discussion.")
                break

    except ConnectionRefusedError:
        print("[-] Serveur introuvable")

    finally:
        client_socket.close()

if __name__ == "__main__":
    demarrer_client()