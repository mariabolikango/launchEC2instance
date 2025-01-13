import time
from datetime import datetime, timedelta

# Fonction pour analyser le fichier de log
def analyze_logs(log_file='server.log'):
    # Lire le fichier de logs
    with open(log_file, 'r') as file:
        logs = file.readlines()

    # Calculer le moment actuel et les deux dernières minutes
    now = datetime.now()
    two_minutes_ago = now - timedelta(minutes=2)

    # Analyser chaque ligne de log
    for log in logs:
        # Extraction de la date et de l'erreur 404 dddddddddddddd
        try:
            # Exemple de format de log: "127.0.0.1 - - [10/Jan/2025 15:30:00] "GET / HTTP/1.1" 200 -"
            date_str = log.split('[')[1].split(']')[0]
             date_str = log.split('[')[1].split(']')[0]
            log_date = datetime.strptime(date_str, "%d/%b/%Y %H:%M:%S")
            status_code = log.split('"')[2].split()[0]

            # Vérifier si l'erreur 404 s'est produite dans les deux dernières minutes
            if status_code == '404' and log_date > two_minutes_ago:
                print(f"Erreur 404 trouvée: {log.strip()}")

        except Exception as e:
            # Ignorer les lignes mal formatées
            continue

if __name__ == '__main__':
    analyze_logs()
