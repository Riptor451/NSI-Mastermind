import doctest
'''
>>> montest(arg1,arg2...)
le résultat attendu
'''

import random

NBTOURMAX = 3
MAXNBCOULEURS = 4
COULEURS = [str(n) for n in range(1,MAXNBCOULEURS+1)]
LONGUEUR = 3
TABULATIONSPACE = ' '*0

# Tâche 9
def est_valide(prop:list)->bool :
    '''
    Fonction booléene qui dit si une séquence correspond à une proposition valide :
    La longueur est bonne et les couleurs sont valides : "1", "2", ... MAXNBCOULEURS
    In : un tableau d'élément de longueur quelconque
    Out : un booléen la longueur de la liste est correct (LONGUEUR) et ses éléments sont des couleurs valides
    >>> LONGUEUR = 3; est_valide(['3','3','5'])
    True
    >>> LONGUEUR = 3; est_valide(['31','3','5'])
    False
    >>> LONGUEUR = 3; est_valide([3,3,5])
    False
    >>> LONGUEUR = 3; est_valide(['3','0','5'])
    False
    >>> LONGUEUR = 4; est_valide(['a','2','5','3'])
    False
    >>> LONGUEUR = 5; est_valide(['1','2','5','3'])
    False
    >>> LONGUEUR = 5; est_valide(['1','2','5','3','1'])
    True
    '''
    pass


# Tâche 10
def entiers_to_combinaison(entree : int) -> list :
    '''
    La fonction convertit un nombre entiers en une combinaison.
    In : un entier (à considérer en base nb de couleurs avec symbole [1..MAXNBCOULEURS]) 
    Out : en sortie une combinaison (list) de chaine de caractères.
    e.g. : entiers_to_combinaison(1215) renvoie ["1","2","1","5"]
    >>> entiers_to_combinaison(1234)
    ['1', '2', '3', '4']
    >>> entiers_to_combinaison(345)
    ['3', '4', '5']
    >>> entiers_to_combinaison(3455788)
    ['3', '4', '5', '5', '7', '8', '8']
    '''
    pass

# Tâche 16
def tour_gagnant(comb : list,numero_de_tour : int) :
    '''
    Procédure :
    Lire une saisie (input) utilisateur : proposition sous forme de nombre à quatre chiffres.
    La transformer en une liste (liste de chiffres comme caractères)
    Tant que cette combinaison n'est pas valide, lire l'input.
    Afficher la proposition en couleur.
    Out : Si la proposition correspond à la combinaison alors renvoyer True, sinon False.
    '''
    pass
    

# Tâche 17
def affiche_message_fin(gagnant : bool) :
    '''
    Affiche un message qui dit que l'utilisateur a gagné 
    Qui propose de rejouer
    Y yes appelle la procédure jeu()
    Toute autre touche ne fait rien, le jeu se termine
    '''
    pass
        
# Tâche 11
def combinaison(l:int) -> list :
    '''
    utilise random.randint
    La fonction combinaison gńére au hasard une combinaison à deviner de longueur l
    In : un entier l (int) qui correspond à la longueur de la combinaison à deviner.
    Out : un tableau (list)
    e.g. : combinaison(4) peut renvoyer ['1','3','5','5'] ou encore ['3','3','6','1'] # si MAXNBCOULEURS vaut 6
    '''
    pass

# Tâche 12
def nb_bien_places(comb:list,prop:list) -> int :
    '''
    La fonction compare une combinaison et une proposition
    (sous forme d'un tableau d'entiers de '1' à '6'.) # si MAXNBCOULEURS vaut 6
    Elle le nombre de couleurs bien placées.
    In : comb et prop, deux tableaux (list) de LONGUEUR caractères entre '1' et '6' # si MAXNBCOULEURS vaut 6 !
    Out : cpt un entier (int) donnant le nombre de couleurs correspondantes.
    >>> nb_bien_places(['1','3','5','5'],['1','2','5','5']) 
    3
    >>> nb_bien_places(['5','5','1','3'],['1','2','5','5']) 
    0
    >>> nb_bien_places(['5','5','1','3','6'],['1','2','5','5','6']) 
    1
    >>> nb_bien_places(['5','5','1','3','6'],['1','3','4','6','5'])
    0
    >>> nb_bien_places(['1','5','4','1','6'],['1','3','4','6','5'])
    2
    '''
    pass


# Tâche 13
def nb_communes(comb:list,prop:list) -> int :
    '''
    La fonction compare une combinaison et une proposition
    (sous forme d'un tableau de LONGUEUR caractères entre '1' et '6') # si MAXNBCOULEURS vaut 6 !
    Elle renvoie le nombre de couleurs en commun qu'elle soit bien ou mal placées.
    In : comb et prop, deux tableaux (list) de LONGUEUR caractères entre '1' et '6' # si MAXNBCOULEURS vaut 6 !
    Out : cpt un entier (int) donnant le nombre de couleurs en commun.
    >>> nb_communes(['1','5','4','1','6'],['1','3','4','6','5'])
    4
    >>> nb_communes(['1','1','4','6'],['1','5','3','2'])
    1
    >>> nb_communes(['2','1','4','6'],['1','5','1','1'])
    1
    >>> nb_communes(['2','1','4','6','6'],['1','6','5','1','1'])
    2
    >>> nb_communes(['2','1','4','6'],['1','2','6','4'])
    4
    >>> nb_communes(['2','1','4','6'],['6','1','4','2'])
    4
    '''
    pass
                
                
    
    
# Tâche 14
def nb_mal_places(comb:list,prop:list) -> int :
    '''
    La fonction compare une combinaison et une proposition
    (sous forme d'un tableau de LONGUEUR caractères entre '1' et '6' # si MAXNBCOULEURS vaut 6 !
    Elle renvoie le nombre de couleurs mal placées.
    In : comb et prop, deux tableaux (list) de LONGUEUR caractères entre '1' et '6' # si MAXNBCOULEURS vaut 6 !
    Out : cpt un entier (int) donnant le nombre de couleurs mal placées.
    >>> nb_mal_places(['2','1','4','6'],['6','1','4','2'])
    2
    >>> nb_mal_places(['2','1','4','6'],['1','2','6','4'])
    4
    >>> nb_mal_places(['2','1','4','6','6'],['1','6','5','1','1'])
    2
    >>> nb_mal_places(['2','1','4','6'],['1','5','1','1'])
    1
    '''
    pass

# Tâche 15
def est_trouve(comb : list,prop : list) -> bool :
    '''
    fonction booléenne qui indique si la proposition correspond à la combinaison
    >>> est_trouve(['1','1','4','6'],['1','1','4','5'])
    False
    >>> est_trouve(['1','1','4','5'],['1','1','4','5'])
    True
    >>> est_trouve(['2','1','4','5'],['1','1','4','5'])
    False
    >>> est_trouve(['1','3','4','5'],['1','1','4','5'])
    False
    '''
    pass

# Tâche 2
def affiche_bandeau_couleurs() :
    '''
    Pour l'utlisateur, affiche les MAXNBCOULEURS couleurs possibles. Sous la forme :
    1■■■  2■■■  3■■■  4■■■
    In : Rien 
    Out : Rien 
    Affichage terminal : voir ci-dessus
    '''
    colors = ""
    for i in range(MAXNBCOULEURS) :
        colors += f"{i}■■■ "
    print(colors)

# Tâche 3
#https://manytools.org/hacker-tools/ascii-banner/
def bienvenu() :
    '''
    Affiche un message de bienvenu avec le titre du jeu et les règles dans le terminal.
    In : Rien 
    Out : Rien 
    Affichage terminal : Le menu du jeu, les règles, le nom du jeu...
    '''
    pass
    
# Tâche 19
def nouvelle_partie() :
    '''
    procédure qui affiche un séparateur de nouvelle partie. La première a été joué.
    In : Rien 
    Out : Rien 
    Affichage terminal : Un message encourageant avant de démarrer la nouvelle partie !
    '''
    print("Un message encourageant avant de démarrer la nouvelle partie !\n----------------------------------------------------------------")




# Tâche 4
def max_len(tab:list[str]) -> int :
    '''
    Prend un tableau(list) avec des lignes de textes(str) et renvoie la longueur de la chaine la plus longue.
    In : Un tableau (list) avec des chaines de caractères.
    Out : Un entier (int) la longueur de la plus longue chaine dans le tableau
    # Interdit d'utiliser une fonction max !
    # Tache  4 : Exemple de tests :
    
    >>> max_len(["bonjour","c'est chouette","l'informatique !"])
    16
    >>> max_len(["t","gjsdg","d","gjsdgdd"])
    7
    >>> max_len(["aaaa","aaa","aa","a",""])
    4
    >>> max_len(["aaaa","aaa","aa","a","","aaa","aa","a","","a","aa"])
    4
    '''
    max = len(tab[0])
    for i in range(len(tab)-1) :
        if len(tab[i]) < len(tab[i+1]) :
            max = len(tab[i+1])
    return max



# Tâche 5
def encadre_tableau_texte(tab:list, bord:int = 1) -> list :
    '''
    Prend un tableau avec des lignes de textes et renvoie une autre liste de chaine de caractères
    qui reprend chaque ligne du tableau mais l'encadre avec des étoiles.
    bord donne l'épaisseur en lignes d'étoiles.
    In : un tableau (list) de chaine de caractères.
    Out : Une tableau (list) de chaine de caractères.
    e.g. :
    
    >>> encadre_tableau_texte( ["Science","Informatique"],2 )
    ["********************",
    "********************",
    "**                **",
    "**                **",
    "**  Science       **",
    "**  Informatique  **",
    "**                **",
    "**                **",
    "********************",
    "********************"]
    >>> encadre_tableau_texte( ["abc","defg"],3 )
    ["****************",
    "****************",
    "****************",
    "***          ***",
    "***          ***",
    "***          ***",
    "***   abc    ***",
    "***   defg   ***",
    "***          ***",
    "***          ***",
    "***          ***",
    "****************",
    "****************",
    "****************"]
    >>> encadre_tableau_texte(["Science","Informatique"],2)
    ["********************","********************","**                **","**                **","**  Science       **","**  Informatique  **","**                **","**                **","********************","********************"]
    >>> encadre_tableau_texte(["ab","abcde","ab"],1)
    ['*********', '*       *', '* ab *', '* abcde *', '* ab *', '*       *', '*********']
    >>> encadre_tableau_texte(["ab","a","ab"],3)
    ['**************', '**************', '**************', '***        ***', '***        ***', '***        ***', '***   ab   ***', '***   a   ***', '***   ab   ***', '***        ***', '***        ***', '***        ***', '**************', '**************', '**************']
    '''
    maxWordLen = max_len(tab)
    for i in range(len(tab)) :
        tab[i] += (maxWordLen - len(tab[i])) * " "

    for i in range(len(tab) + 2 * bord) :
        if (i > bord and i < (len(tab) - bord)) :
            if (i > bord * 2 and i < (len(tab) - bord * 2)) :
                print("*" * bord, "0" * bord, tab[i], " " * bord, "*" * bord)

    for i in range(bord * 2 * len(tab)) :
        print("*" * (maxWordLen + 2 * bord))
    


# Tâche 6
def tableau_to_chaine(tab:list) -> str :
    '''
    La fonction met bout à bout les chaines de caractères contenues dans un tableau.
    Il y a des retours chariot (\n) entre chaque ligne
    In : Un tableau(list) de chaines de caractères
    Out : Une chaine de caractère qui concatène les éléments du tableau avec un retour-chariot entre chaque.
    e.g. :
    en entrée :["Numérique","Science","Informatique"]
    en sortie : "Numérique\nScience\nInformatique"
    tests :
    
    >>> tableau_to_chaine(["Numérique","Science","Informatique"])
    'Numérique\nScience\nInformatique'
    >>> tableau_to_chaine(["a","toto","foo","fi"])
    'a\ntoto\nfoo\nfi'
    >>> tableau_to_chaine(["Projet :","","MasterMind","Ada Lovelace"])
    'Projet :\n\nMasterMind\nAda Lovelace'
    '''
    pass


# Tâche 7
# https://www.commentcoder.com/python-couleur/
# https://www.asciiart.eu/ascii-draw-studio/app
def affiche_proposition(prop:list,nbbp:int,nbmp:int,nbessai:int) :
    '''
    la procédure affiche dans le terminal la combinaison en couleur.
    Puis le nbbp, nombre bien placés, et le nbmp nombre mal placés, le numero du tour
    et place le prompt pour le prochain essai
    In : un tableau (list) formés de LONGUEUR caractères entre '1' et '6' # si MAXNBCOULEURS vaut 6 !
    Out : rien
    Affichage terminal :
    e.g : si prop est ['2','4','5','6'], nbbp vaut 2 et nbmp vaut 1
    
    >>> affiche_proposition( ['2','4','5','6'], 2, 1
    2■■■  4■■■  5■■■  6■■■   BP : 2   MP : 1   tour : 1   suivant ?>
    '''
    print('Voilà la correspondance pour les couleurs !')
    print("\033[31m ROUGE : 1 "+ chr(0x25A0) ,end='  - ')
    print("\033[32m VERT : 2 " + chr(0x25A0) ,end='  - ')
    print("\033[33m JAUNE : 3 " + chr(0x25A0),end='  - ')
    print("\033[34m BLEU : 4 " + chr(0x25A0),end='  - ')
    print("\033[35m VIOLET : 5 " + chr(0x25A0),end='  - ')
    print("\033[36m CIEL : 6 " + chr(0x25A0),end='  - ')


# Tâche 8
def affiche_combinaison(comb:list) :
    '''
    la fonction affiche dans le terminal la combinaison en couleur.
    In : un tableau (list) formés de LONGUEUR caractères entre '1' et '6' # si MAXNBCOULEURS=6
    Out : rien
    Affichage terminal :
    e.g : e.g : si prop est ['2','4','5','6']
    
    >>> affiche_combinaison(['2','4','5','6'])
    2■■■  4■■■  5■■■  6■■■  

    print('Voilà la correspondance pour les couleurs !')
    print("\033[31m ROUGE : 1 "+ chr(0x2B1B) ,end='  - ')
    print("\033[32m VERT : 2 " + chr(0x2B1B) ,end='  - ')
    print("\033[33m JAUNE : 3 " + chr(0x2B1B),end='  - ')
    print("\033[34m BLEU : 4 " + chr(0x2B1B),end='  - ')
    print("\033[35m VIOLET : 5 " + chr(0x2B1B),end='  - ')
    print("\033[36m CIEL : 6 " + chr(0x2B1B),end='  - ')
    '''
    pass

# Tâche 18
def jeu(premier : bool = True ) -> None :
    '''
    La procédure lance un nouveau jeu, si premier est vrai, alors c'est le premier lancement du jeu.
    Sinon, le joueur a déjà joué et a choisi de continuer.
    Le jeu se déroule, en cas de victoire on félicite le joueur !
    Si le nombre de tour effectuées atteint NBTOURMAX, le joueur a perdu.
    Dans tous les cas on propose de continuer ou non avec un nouveau jeu...
    In : un booléen pour distinguer les deux cas
    Out : rien
    '''
    print(f"game as started with premier == {premier}")
    # Affichage du bon bandeau
    pass
    # Choix de la combinaison à deviner / initialisation du numero de tours
    pass
    # Boucle de jeu 
    pass

