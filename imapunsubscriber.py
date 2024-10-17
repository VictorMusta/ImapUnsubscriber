import imaplib
import email
from bs4 import BeautifulSoup
import requests

# Remplacez les valeurs par votre adresse mail et votre mot de passe
# Attention: l'utilisation de votre mot de passe principal n'est pas recommandée pour des raisons de sécurité.


# Pour une adresse Gmail:
# Je vous conseille de créer un "mot de passe d'application" sur votre compte google
# afin de ne pas utiliser votre mot de passe principal.
# Pour cela, rendez-vous sur https://myaccount.google.com/security-checkup
# cliquez sur "Mot de passe d'application" dans la section "Connexion à Google".
# Créez un mot de passe d'application pour l'application "Autre (nom personnalisé)".
# Utilisez ce mot de passe d'application pour vous connecter à votre boîte mail.
your_email = 'TEMPLATE'
your_password = 'TEMPLATE'

# WARNING : De nombreux sites web malveillants utilisent des liens de désabonnement pour envoyer ses malwares / ransomwares.
# Veuillez utiliser ce script avec précaution et vérifier que les liens de désabonnement sont bien légitimes.
# Ce script ne les vérifiera pas
# et les suivra aveuglément.
# Il est recommandé de vérifier manuellement les liens de désabonnement avant de les suivre.

# Connexion à la boîte mail
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(your_email, your_password)
mail.select('inbox')

# Recherche des emails contenant "unsubscribe"
status, messages = mail.search(None, '(BODY "unsubscribe")')

# Extraction des liens de désabonnement
for num in messages[0].split():
    status, data = mail.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                soup = BeautifulSoup(part.get_payload(decode=True), 'html.parser')
                for link in soup.find_all('a', href=True):
                    if 'unsubscribe' in link['href']:
                        unsubscribe_link = link['href']
                        # Automatisation du désabonnement
                        response = requests.get(unsubscribe_link)
                        if response.status_code == 200:
                            print(f'Désabonné avec succès de {unsubscribe_link}')
                        else:
                            print(f'Échec du désabonnement de {unsubscribe_link}')

# Déconnexion de la boîte mail
mail.logout()
