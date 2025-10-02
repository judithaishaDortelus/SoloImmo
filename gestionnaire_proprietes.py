"""
Ce module est responsable de la gestion des propriétés dans l'application IFT-1004 Solo Immo,
incluant l'ajout de nouvelles propriétés, la liste et le filtrage des propriétés disponibles.

Fonctions:
- `lister_proprietes()`: Liste toutes les propriétés disponibles.
- `filtrer_proprietes()`: Filtre les propriétés en fonction des critères de l'utilisateur.
- `ajouter_propriete()`: Ajoute une nouvelle propriété si l'utilisateur est connecté.

Dépendances:
- `gestionnaire_donnees`: Pour lire et écrire dans le fichier des propriétés.
- `gestionnaire_utilisateurs`: Pour vérifier si un utilisateur est connecté.
- `utilitaires`: Pour des fonctions auxiliaires comme l'affichage de tableaux formatés,
et le formatage de montants en dollars.
"""
from configuration import FICHIER_PROPRIETES
from gestionnaire_donnees import charger_proprietes, sauvegarder_propriete
from gestionnaire_utilisateurs import utilisateur_est_connecte, recuperer_utilisateur_courant
from utilitaires import afficher_tableau, formater_argent, garantir_existence_fichier

TYPES_DE_PROPRIETE = ["Maison", "Appartement", "Condo", "Loft"]
VILLES = ["Québec", "Montréal", "Toronto", "Ottawa"]


def lister_proprietes():
    """Affiche la liste de toutes les propriétés disponibles sous forme de tableau.

    Cette fonction suit les étapes suivantes :
      1. Charge les propriétés à partir du fichier de données via la fonction `charger_proprietes`.
      2. Si aucune propriété n'est disponible, affiche un message indiquant "Aucune propriété disponible".
      3. Si des propriétés sont disponibles, formate chaque propriété en une ligne de tableau avec les colonnes suivantes :
         - Prix : formaté en devise grâce à `formater_argent`.
         - Ville : ville où se situe la propriété.
         - Type de propriété : type (par exemple, Maison, Condo).
         - Chambres : nombre de chambres.
         - Salles de bains : nombre de salles de bains.

    Les informations sont ensuite affichées dans un tableau formaté avec une ligne d'en-tête descriptive.

    Affiche un message approprié si aucune propriété n'est disponible.
    """
    if not utilisateur_est_connecte():
        return print("Aucune propriété disponible.")

    while utilisateur_est_connecte():
        proprietes_existants = charger_proprietes()

        if not proprietes_existants:
            return print("Aucune propriété disponible")

        en_tetes = ["Prix", "Ville", "Type de propriété", "Chambres", "Salle de bains"]
        chaque_ligne = []

        for propriete in proprietes_existants:
            propriete["prix"] = formater_argent(float(propriete["prix"]))
            ligne = list(propriete.values())
            chaque_ligne.append(ligne)

        return afficher_tableau(chaque_ligne, en_tetes)


def filtrer_proprietes():
    """Filtre les propriétés disponibles selon les critères définis par l'utilisateur.

    Cette fonction permet de rechercher des propriétés en appliquant des filtres basés sur les critères suivants :
      1. Prix (minimum et maximum)
      2. Ville
      3. Type de propriété (ex. Maison, Condo)
      4. Nombre de chambres
      5. Nombre de salles de bains
      6. Combinaison de plusieurs de ces critères

    Processus de filtrage :
      - Affiche un menu permettant à l'utilisateur de sélectionner un critère de filtrage unique
        ou une combinaison de critères.
      - En fonction de l'option choisie, invite l'utilisateur à entrer les valeurs de filtrage.
      - Applique les critères pour trouver les propriétés correspondantes.

    Affichage :
      - Si des propriétés correspondant aux critères sont trouvées, elles sont affichées sous forme de tableau
        avec les colonnes : Prix, Ville, Type de propriété, Chambres, et Salles de bains.
      - Si aucune propriété ne correspond, un message indique qu'aucune propriété n'est disponible.
    """
    if not utilisateur_est_connecte():
        return print("Aucune propriété disponible.")

    while utilisateur_est_connecte():
        proprietes_existants = charger_proprietes()

        if not proprietes_existants:
            return print("Aucune propriété disponible")

        continuer = True
        while continuer:
            print("\nOptions de filtrage:")
            print("1. Filtrer par prix")
            print("2. Filtrer par ville")
            print("3. Filtrer par type de propriété")
            print("4. Filtrer par nombre de chambres")
            print("5. Filtrer par nombre de salles de bains")
            print("6. Filtrer par une combinaison des options")

            choix = input("Choisissez une option de filtrage: ")

            if choix not in "123456":
                print("Option invalide.")
                return False

            en_tetes = ["Prix", "Ville", "Type de propriété", "Chambres", "Salle de bains"]
            filtrage = []

            if choix == "1":
                prix_minimum, prix_maximum = demander_plage_de_prix(optionnel=True)
                for propriete in proprietes_existants:
                    propriete_copie_pour_affichage = propriete.copy()
                    prix = propriete_copie_pour_affichage["prix"]
                    if (prix_minimum is None or prix >= prix_minimum) and (prix_maximum is None or prix <= prix_maximum):
                        filtrage.append(propriete_copie_pour_affichage)
                        propriete_copie_pour_affichage["prix"] = formater_argent(float(propriete_copie_pour_affichage["prix"]))

                lignes = [list(propriete_copie_pour_affichage.values()) for propriete_copie_pour_affichage in filtrage]
                afficher_tableau(lignes, en_tetes)
                return False

            elif choix == "2":
                ville_choisie = demander_ville()

                for propriete in proprietes_existants:
                    if ville_choisie and propriete["ville"] == ville_choisie:
                        filtrage.append(propriete)

                if not filtrage:
                    print("Aucune propriété n'est disponible.")
                    return False
                else:
                    for propriete in filtrage:
                        propriete["prix"] = formater_argent(float(propriete["prix"]))

                lignes = [list(propriete.values()) for propriete in filtrage]
                afficher_tableau(lignes, en_tetes)
                return False

            elif choix == "3":
                type_propriete = demander_type_de_propriete()

                for propriete in proprietes_existants:
                    if type_propriete and propriete["type"] == type_propriete:
                        filtrage.append(propriete)

                if not filtrage:
                    print("Aucune propriété n'est disponible.")
                    return False
                else:
                    for propriete in filtrage:
                        propriete["prix"] = formater_argent(float(propriete["prix"]))

                lignes = [list(propriete.values()) for propriete in filtrage]
                afficher_tableau(lignes, en_tetes)
                return False

            elif choix == "4":
                chambres_choisies = demander_nombre_positif("Nombre de chambres")

                for propriete in proprietes_existants:
                    if chambres_choisies and propriete["chambres"] == chambres_choisies:
                        filtrage.append(propriete)

                if not filtrage:
                    print("Aucune propriété n'est disponible.")
                    return False
                else:
                    for propriete in filtrage:
                        propriete["prix"] = formater_argent(float(propriete["prix"]))

                lignes = [list(propriete.values()) for propriete in filtrage]
                afficher_tableau(lignes, en_tetes)
                return False

            elif choix == "5":
                salles_de_bains_choisies = demander_nombre_positif("Nombre de salles de bains")
                for propriete in proprietes_existants:
                    if salles_de_bains_choisies and propriete["salles_de_bains"] == salles_de_bains_choisies:
                        filtrage.append(propriete)

                if not filtrage:
                    print("Aucune propriété n'est disponible.")
                    return False
                else:
                    for propriete in filtrage:
                        propriete["prix"] = formater_argent(float(propriete["prix"]))

                lignes = [list(propriete.values()) for propriete in filtrage]
                afficher_tableau(lignes, en_tetes)
                return False

            elif choix == "6":
                prix_minimum, prix_maximum = demander_plage_de_prix(optionnel=True)
                ville_choisie = demander_ville(optionnel=True)
                type_propriete = demander_type_de_propriete(optionnel=True)
                chambres_choisies = demander_nombre_positif("Nombre de chambres", optionnel=True)
                salles_de_bains_choisies = demander_nombre_positif("Nombre de salles de bains", optionnel=True)

                for propriete in proprietes_existants:
                    propriete_copie_pour_affichage = propriete.copy()
                    prix = propriete_copie_pour_affichage["prix"]
                    critere_choisie = True

                    if prix_minimum is not None and prix < prix_minimum:
                        critere_choisie = False
                    if prix_maximum is not None and prix > prix_maximum:
                        critere_choisie = False
                    if ville_choisie and propriete_copie_pour_affichage["ville"] != ville_choisie:
                        critere_choisie = False
                    if type_propriete and propriete_copie_pour_affichage["type"] != type_propriete:
                        critere_choisie = False
                    if chambres_choisies and propriete_copie_pour_affichage["chambres"] != chambres_choisies:
                        critere_choisie = False
                    if salles_de_bains_choisies and propriete_copie_pour_affichage["salles_de_bains"] != salles_de_bains_choisies:
                        critere_choisie = False

                    if critere_choisie:
                        filtrage.append(propriete_copie_pour_affichage)
                        propriete_copie_pour_affichage["prix"] = formater_argent(float(propriete_copie_pour_affichage["prix"]))

                if filtrage:
                    lignes = [list(propriete.values()) for propriete in filtrage]
                    afficher_tableau(lignes, en_tetes)
                    return False
                else:
                    print("Aucune propriété n'est disponible.")
                    return False


def ajouter_propriete():
    """Ajoute une nouvelle propriété à la liste des propriétés, si l'utilisateur est connecté.

    Cette fonction suit les étapes suivantes :
      1. Vérifie si un utilisateur est connecté en appelant `utilisateur_est_connecte`.
         Si aucun utilisateur n'est connecté, affiche un message d'erreur et interrompt le processus.
      2. Demande les informations détaillées de la propriété à ajouter, en incluant :
         - Prix (valeur positive)
         - Ville
         - Type de propriété (par exemple, Maison, Condo)
         - Nombre de chambres (valeur positive)
         - Nombre de salles de bains (valeur positive)
      3. Enregistre les informations de la nouvelle propriété dans le fichier de propriétés via la fonction `sauvegarder_propriete`.

    Affiche un message de confirmation une fois la propriété ajoutée, ou un message d'erreur si l'utilisateur n'est pas connecté.
    """
    nouvelle_propriete = charger_proprietes()

    if utilisateur_est_connecte():
        prix = demander_nombre_positif("Prix")
        ville = demander_ville()
        type_propriete = demander_type_de_propriete()
        chambres = demander_nombre_positif("Nombre de chambres")
        salles_de_bains = demander_nombre_positif("Nombre de salles de bains")

        nouvelle_propriete = {"prix": prix, "ville": ville, "type": type_propriete, "chambres": chambres, "salles_de_bains": salles_de_bains}
        print("Propriété ajoutée avec succès.")
    return sauvegarder_propriete(nouvelle_propriete)

def demander_plage_de_prix(optionnel=False):
    """Demande à l'utilisateur de saisir une plage de prix.

    Args:
        optionnel (bool): Indique si la saisie est facultative.

    Returns:
        tuple: (prix_minimum, prix_maximum)
    """
    while True:
        try:
            prix_minimum = input("Prix minimum: ")
            prix_maximum = input("Prix maximum: ")
            if optionnel and not prix_minimum and not prix_maximum:
                return None, None
            prix_minimum = int(prix_minimum) if prix_minimum else None
            prix_maximum = int(prix_maximum) if prix_maximum else None
            if (
                prix_minimum is not None
                and prix_maximum is not None
                and prix_minimum > prix_maximum
            ):
                raise ValueError(
                    "Le prix minimum doit être inférieur ou égal au prix maximum."
                )
            return prix_minimum, prix_maximum
        except ValueError as e:
            print(e)


def demander_ville(optionnel=False):
    """Demande à l'utilisateur de choisir une ville parmi les choix définis.

    Args:
        optionnel (bool): Indique si la saisie est facultative.

    Returns:
        str: La ville choisie.
    """
    print(f"Choisissez une ville parmi les suivantes: {', '.join(VILLES)}")
    while True:
        ville = input("Ville: ").capitalize()
        if optionnel and not ville:
            return None
        if ville in VILLES:
            return ville
        print(f"Ville invalide. Choisissez parmi: {', '.join(VILLES)}")


def demander_type_de_propriete(optionnel=False):
    """Demande à l'utilisateur de choisir un type de propriété parmi les choix définis.

    Args:
        optionnel (bool): Indique si la saisie est facultative.

    Returns:
        str: Le type de propriété choisi.
    """
    print(
        f"Choisissez un type de propriété parmi les suivants: {', '.join(TYPES_DE_PROPRIETE)}"
    )
    while True:
        type_de_propriete = input("Type de propriété: ").capitalize()
        if optionnel and not type_de_propriete:
            return None
        if type_de_propriete in TYPES_DE_PROPRIETE:
            return type_de_propriete
        print(
            f"Type de propriété invalide. Choisissez parmi: {', '.join(TYPES_DE_PROPRIETE)}"
        )


def demander_nombre_positif(prompt, optionnel=False):
    """Demande à l'utilisateur de saisir un nombre positif.

    Args:
        prompt (str): Le message à afficher pour la saisie.
        optionnel (bool): Indique si la saisie est facultative.

    Returns:
        int: Le nombre saisi, qui sera positif.
    """
    while True:
        nombre = input(f"{prompt}: ")
        if optionnel and not nombre:
            return None
        try:
            nombre = int(nombre)
            if nombre > 0:
                return nombre
            else:
                print("Veuillez saisir un nombre positif.")
        except ValueError:
            print("Valeur invalide. Veuillez saisir un nombre.")
