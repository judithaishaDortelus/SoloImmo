# SoloImmo 
Application console en Python simulant une plateforme immobilière, développée avec des mécanismes permettant la gestion des comptes utilisateurs ainsi que l'ajout, la consultation et le filtrage des propriétés. Projet réalisé dans le cadre d'un cours à l'Université Laval.

### Fonctionnalités principales:
- Création et authentification sécurisée des comptes
- Hachage des mots de passe avec l'algorithme SHA-256
- Ajout, affichage et filtrage de propriétés immobilières
- Association des propriétés aux comptes utilisateurs
- Système de connexion et déconnexion

### Technologies utilisées:
- Python
- hashlib
- secrets

### Aperçu de l'application SoloImmo:
#### Création de compte et connexion
L'utilisateur doit créer un compte et s'y connecter pour accéder aux fonctionnalités. Le nom d'utilisateur et mot de passe (haché avec SHA-256) sont sauvegardés dans un fichier texte (.txt).
<img width="497" height="257" alt="01" src="https://github.com/user-attachments/assets/f9a92f18-86aa-462d-9b89-dfe463395aa3" />
<img width="354" height="231" alt="02" src="https://github.com/user-attachments/assets/1f983f34-1c56-4dff-9166-bd1deb6058f5" />
<img width="350" height="419" alt="03" src="https://github.com/user-attachments/assets/4d3ad5dd-4e71-428d-88fd-ae98a835a575" />

#### Ajouter, lister et filtrer des propriétés
L'utilisateur peut consulter, lister et filtrer à travers les propriétés qui ont été ajoutés à son compte.
<img width="735" height="339" alt="04" src="https://github.com/user-attachments/assets/396155c4-07f4-4bf6-8da9-e2755274f5f6" />
<img width="712" height="406" alt="05" src="https://github.com/user-attachments/assets/f40023ad-e5af-45bc-8a0b-9d20abba1b37" />
<img width="657" height="387" alt="06" src="https://github.com/user-attachments/assets/e0ad3d71-e182-4510-9902-bf29177f7d50" />


#### Déconnexion et quitter
Lorsque l'utilisateur se déconnecte, les informations reliées à son compte sont conservés. Les données sont conservés entre les sessions.
<img width="609" height="396" alt="07" src="https://github.com/user-attachments/assets/1868ce1b-9f8a-47d2-b93a-1efd7a97156c" />
