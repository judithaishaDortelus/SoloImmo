# SoloImmo
Application console en Python simulant une plateforme immobilière. Elle permet la gestion des comptes utilisateurs (inscription, connexion, deconnexion, mots de passe hachés) ainsi que l'ajout, la consultation et le filtrage des propriétés. Réalisé dans le cadre d'un cours à l'Université Laval.

### Principales fonctionnalités:
- Création et authentification sécurisé des utilisateurs
- Ajout, affichage et filtrage de propriétés immobilières

### Technologies utilisées:
- Python
- hashlib
- secrets

### Aperçu de l'application SoloImmo:
#### Créer un compte et se connecter
L'utilisateur doit se créer un compte et se connecter pour ajouter des propriétés. L'algorithme de hachage SHA-256 est utilisé pour sauvegarder le mot de passe de l'utilisateur. Le compte est sauvegardé dans un fichier .txt.
<img width="497" height="257" alt="01" src="https://github.com/user-attachments/assets/f9a92f18-86aa-462d-9b89-dfe463395aa3" />
<img width="354" height="231" alt="02" src="https://github.com/user-attachments/assets/1f983f34-1c56-4dff-9166-bd1deb6058f5" />
<img width="350" height="419" alt="03" src="https://github.com/user-attachments/assets/4d3ad5dd-4e71-428d-88fd-ae98a835a575" />

#### Ajouter, lister et filtrer des propriétés
L'utilisateur lister et filtrer à travers les propriétés qui ont été ajoutés à son compte.
<img width="735" height="339" alt="04" src="https://github.com/user-attachments/assets/396155c4-07f4-4bf6-8da9-e2755274f5f6" />
<img width="712" height="406" alt="05" src="https://github.com/user-attachments/assets/f40023ad-e5af-45bc-8a0b-9d20abba1b37" />
<img width="657" height="387" alt="06" src="https://github.com/user-attachments/assets/e0ad3d71-e182-4510-9902-bf29177f7d50" />


#### Se déconnecter et quitter
L'utilisateur peut se déconnecter et/ou quitter et les informations reliées à son compte seront conservés.
<img width="609" height="396" alt="07" src="https://github.com/user-attachments/assets/1868ce1b-9f8a-47d2-b93a-1efd7a97156c" />
