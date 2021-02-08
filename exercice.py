def chargement():
    """
    Cette fonction charge en mémoire le contenu de la base de données des adresses enregistrées.
    """
    # TODO: initialiser la structure de données vide

    with open('data/database.txt', mode='r') as f:
        file_rows = f.readlines()
        for row in file_rows: 
            type, nom, annee = nettoyer(row)

            # TODO: Tester le type du média et l'ajouter a la bonne structure de données

    return ...


def nettoyer(ligne):
	
	#TODO: séparer la ligne reçue en paramètre en trois variables 
	# type : pour le type du média
	# nom  : Pour le nom du média
	# annee: pour l'année de production du média
	
	
	# TODO: remplacer le caractère _ dans le nom du média par un espace
    

    return ...


def chercher(film_donnees, serie_donnees):
	
	# TODO: demander à l'utilisateur de saisir un type de média à rechercher
	# l'utilisateur continue de faire la saisie tant que type ne correspond pas à (film ou série)
	
	
	# TODO: demander à l'utilisateur de saisir le nom du média rechercher
	
	
	# TODO: dépendamment du type du média rechercher, on doit chercher le nom du média rechercher dans la bonne
	# structure de données
 
	
	# TODO: afficher l'ensemble des médias qui contient le nom recherché
	
	
	# TODO: la fonction retourne True si on trouve au moins un seul média, false sinon


    return ...


if __name__ == '__main__':
    film_donnees, serie_donnees = chargement()
    chercher(film_donnees, serie_donnees)
	