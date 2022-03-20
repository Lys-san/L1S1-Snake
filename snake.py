from upemtk import *
from time import sleep
from random import *
from doctest import *

# dimensions du jeu
taille_case = 20
largeur_plateau = 30  # en nombre de cases
hauteur_plateau = 18  # en nombre de cases
x_fenetre = taille_case * largeur_plateau
y_fenetre = taille_case * hauteur_plateau
aire = x_fenetre * y_fenetre


def gif_ecran_titre():
    '''
    animation lors du lancer du jeu
    '''
    
    x = x_fenetre / 6
    y = y_fenetre / 2
    for i in range (43):
        file = 'sprite_'+str(i)+'.png'
        sprite = image(3 * x, y + x / 4, file, ancrage='center')
        attente(0.07)
        efface(sprite)
    file = 'sprite_43.png'
    for i in range(10):
        sprite = image(3 * x, (y + x / 4)-5*i, file, ancrage='center')
        attente(0.03)
        efface(sprite)
    sprite = image(3 * x, (y + x / 4)-50, file, ancrage='center')


def affiche_ecran_titre(x, y):
    '''
    affiche un écran titre centré lors du lancer du jeu
    prend en paramètre les dimensions en pixel de la fenêtre 
    renvoie les coordonées des rectangles contenant les trois boutons 
    ('Jouer', 'Options' et 'Quitter')
    
    >>> affiche_ecran_titre(600, 400)
    100, 200, 250, 350, 400, 500, 266 + 2 / 3, 316 + 2 / 3 
    '''
    image(x/2, y/2, 'backmenu.gif', ancrage = 'center')
    gif_ecran_titre()
    # proportions des boutons:
    bx = x_fenetre / 6
    by = y_fenetre / 1.5
    
    # bouton 'Jouer'
    texte(1.5 * bx, by + bx / 4, 'JOUER ', ancrage = 'center', 
          couleur = 'yellow', taille = 20)
    
    # bouton 'Paramètres'
    texte(3 * bx, by + bx / 4, 'OPTIONS ', ancrage = 'center', 
          couleur = 'yellow', taille = 20)
    
    # bouton 'Quitter'
    texte(4.5 * bx, by + bx / 4, ' QUITTER', ancrage = 'center', 
          couleur = 'yellow', taille = 20)
    
    return bx, 2 * bx, 2.5 * bx, 3.5 * bx, 4 * bx, 5 * bx, by, by + bx / 2

    
def clic_choix_parametre_vitesse(x, y, xclic, yclic, vitesse):
    a, b, c = y / 8, x / 8, x / 12 
    #choix du peramètre vitesse
    if yclic > 2*a and yclic < 3*a:
        if xclic > 3*b and xclic < 3*b + 2*c:
            return ['red', 'yellow', 'yellow']
        elif xclic > 3*b + 2*c and xclic < 5*b + c:
            return ['yellow', 'red', 'yellow']
        elif xclic > 5*b + c and xclic < 7*b:
            return ['yellow', 'yellow', 'red']
        else: 
            return vitesse
    else:
        return vitesse
    
def clic_choix_parametre_pomme(x, y, xclic, yclic, pommes):
    a, b, c = y / 8, x / 8, x / 12 
    #choix du parametre pomme
    if yclic > 3*a and yclic < 4*a:
        if xclic > 3*b and xclic < 5*b:
            return ['red', 'yellow']
        elif xclic > 5*b and xclic < 7*b:
            return ['yellow', 'red']
        else: 
            return pommes

    else:
        return pommes
    
    
def clic_choix_parametre_arene(x, y, xclic, yclic, arene):
    a, b, c = y / 8, x / 8, x / 12 
    #choix du peramètre arene
    if yclic > 4*a and yclic < 5*a:
        if xclic > 3*b and xclic < 3*b + 2*c:
            return ['red', 'yellow', 'yellow']
        elif xclic > 3*b + 2*c and xclic < 5*b + c:
            return ['yellow', 'red', 'yellow']
        elif xclic > 5*b + c and xclic < 7*b:
            return ['yellow', 'yellow', 'red']
        else:
            return arene
    else:
        return arene
    
        
def clic_choix_parametre_couleur(x, y, xclic, yclic, couleur):
    a, b, c = y / 8, x / 8, x / 12 
    #choix du parametre couleur
    if yclic > 5*a and yclic < 6*a:
        if xclic > 3*b and xclic < 4*b:
            return ['red', 'yellow', 'yellow', 'yellow']
        elif xclic > 4*b and xclic < 5*b:
            return ['yellow', 'red', 'yellow', 'yellow']
        elif xclic > 5*b and xclic < 6*b:
            return ['yellow', 'yellow', 'red', 'yellow']
        elif xclic > 6*b and xclic < 7*b:
            return ['yellow', 'yellow', 'yellow', 'red']
        else: 
            return couleur
    else:
        return couleur
    
    
def clic_choix_parametre_plus(x, y, xclic, yclic, truc):
    a, b, c = y / 8, x / 8, x / 12 
    truc_1 = list(truc)
    #options en +
    if yclic > 6*a and yclic < 7*a:
        if xclic > 3*b and xclic < 5*b:
            if truc[0] == 'red': 
                truc_1[0] = 'yellow'
            elif truc[0] == 'yellow':
                truc_1[0] = 'red' 
            
        elif xclic > 5*b and xclic < 7*b:
            if truc[1] == 'red': 
                truc_1[1] = 'yellow'
            elif truc[1] == 'yellow':
                truc_1[1] = 'red'
        
    return truc_1
    
    
def clic_choix_parametre_sortie(x, y, xclic, yclic):
    a, b, c = y / 8, x / 8, x / 12 
    #retour à l'écran titre ou début d'une nouvelle partie
    if yclic > 7*a and yclic < 8*a:
        if xclic > 3*b and xclic < 5*b:
            return True
        else: 
            return False
    else:
        return False
    
    
def init_param():
    framerate = 10
    torique = False
    openworld = False
    obstacles = True
    bombes = True
    pommes_multiples = False
    couleur = 'green'
    return (framerate, pommes_multiples, torique, openworld, couleur, 
            obstacles, bombes)
    
    
def init_menu():
    vitesse = ['yellow', 'red', 'yellow']
    pommes = ['red', 'yellow']
    arene = ['red', 'yellow', 'yellow']
    couleur = ['red', 'yellow', 'yellow', 'yellow']
    truc = ['red', 'red']
    return vitesse, pommes, arene, couleur, truc

    
def renvoi_parametres(x, y, choix, vitesse, pommes, arene, couleur, truc):
    if vitesse[0] == 'red':
        framerate = 5 
    elif vitesse[1] == 'red':
        framerate = 20
    elif vitesse[2] == 'red':
        framerate = 40
    
    if pommes[0] == 'red':
        pommes_multiples = False
    elif pommes[1] == 'red':
        pommes_multiples = True
        
    if arene[0] == 'red':
        torique = False
        openworld = False
    elif arene[1] == 'red':
        torique = True
        openworld = False
    elif arene[2] == 'red':
        torique = False
        openworld = True
        
    if couleur[0] == 'red':
        couleur = 'green'
    elif couleur[1] == 'red':
        couleur = 'white'
    elif couleur[2] == 'red':
        couleur = 'purple'
    elif couleur[3] == 'red':
        couleur = 'multicolore'
        
    if truc[0] == 'red':
        obstacles = True
    else:
        obstacles = False
        
    if truc[1] == 'red':
        bombes = True
    else: 
        bombes = False
        
    return (framerate, pommes_multiples, torique, openworld, 
            couleur, obstacles, bombes)
    

def affiche_menu_option(x, y, choix):
    '''
    affiche un menu réparti 'harmonieusement' sur toute la surface de la 
    fenêtre
    prend comme paramètre les dimensions en pixel de la fenêtre (x et y)
    le paramètre 'choix' correspond au bouton de sortie des options: 'MENU' 
    (si on accède à Options depuis l'écran titre) 
    ou 'REJOUER' (si on accède à Options depuis l'écran de game over)
    '''
    efface_tout()
    a, b, c = y / 8, x / 8, x / 12 
    #affichage des textes
    image(x/2, y/2, 'backmenu.gif', ancrage = 'center')
    texte(x / 2, a, 'OPTIONS', ancrage = 'center', 
          couleur = 'yellow', taille = 40)

    texte(2 * b, 2.5 * a, 'Vitesse du serpent:', ancrage = 'center', 
          couleur = 'yellow', taille = 12)

    texte(3 * b + c, 2.5 * a, 'lente', ancrage = 'center', 
          couleur = vitesse[0], taille = 12)
    texte(5 * b, 2.5 * a, 'moyenne', ancrage = 'center', 
          couleur = vitesse[1], taille = 12)
    texte(5 * b + 2 * c, 2.5 * a, 'rapide', ancrage = 'center', 
          couleur = vitesse[2], taille = 12)
    
    texte(2 * b, 3.5 * a, 'Pommes:', ancrage = 'center', 
          couleur = 'yellow', taille = 12)
    
    texte(4 * b , 3.5 * a, 'classique', ancrage = 'center', 
          couleur = pommes[0], taille = 12)
    texte(6 * b , 3.5 * a, 'multiples', ancrage = 'center', 
          couleur = pommes[1], taille = 12)
    
    texte(2 * b, 4.5 * a, 'Arène:', ancrage = 'center', 
          couleur = 'yellow', taille = 12)
    
    texte(3 * b + c, 4.5 * a, 'normale', ancrage = 'center', 
          couleur = arene[0], taille = 12)
    texte(5 * b, 4.5 * a, 'torique', ancrage = 'center', 
          couleur = arene[1], taille = 12)
    texte(5 * b + 2 * c, 4.5 * a, 'infinie', ancrage = 'center', 
          couleur = arene[2], taille = 12)

    texte(2 *b, 5.5 * a, 'Couleur', ancrage = 'center', 
          couleur = 'yellow', taille = 12 )
    
    texte(3.5 * b, 5.5 * a, 'vert', ancrage = 'center', 
          couleur = couleur[0], taille = 12)
    texte(4.5 * b, 5.5 * a, 'blanc', ancrage = 'center', 
          couleur = couleur[1], taille = 12)
    texte(5.5 * b, 5.5 * a, 'violet', ancrage = 'center', 
          couleur = couleur[2], taille = 12)
    texte(6.5 * b, 5.5 * a, '???', ancrage = 'center', 
          couleur = couleur[3], taille = 12)
    
    texte(2*b, 6.5*a, 'Trucs en +', ancrage = 'center', 
          couleur = 'yellow', taille = 12 )
    
    texte(4*b, 6.5 * a, 'obstacles', ancrage = 'center', 
          couleur = truc[0], taille = 12)
    texte(6*b, 6.5 * a, 'missiles', ancrage = 'center', 
          couleur = truc[1], taille = 12)
    
    #bouton retour à l'écran titre
    texte(x / 2, 7.3 * a , choix, ancrage = 'center', 
          couleur = 'red', taille = 14)  
    
    mise_a_jour()
    
    
def menu_option(x, y, choix, vitesse, pommes, arene, couleur, truc):
    ''' 
    gère la couleur d'affichage des options (rouge si elles sont actives, 
    jaunes sinon)
    '''
    affiche_menu_option(x, y, choix)

    #gestion des clics de l'utilisateur
    xclic, yclic = attend_clic_gauche()
    vitesse = clic_choix_parametre_vitesse(x, y, xclic, yclic, vitesse)
    pommes = clic_choix_parametre_pomme(x, y, xclic, yclic, pommes)
    arene = clic_choix_parametre_arene(x, y, xclic, yclic, arene)
    couleur = clic_choix_parametre_couleur(x, y, xclic, yclic, couleur)
    truc = clic_choix_parametre_plus(x, y, xclic, yclic, truc)
 
    sortie = clic_choix_parametre_sortie(x, y, xclic, yclic)
    return vitesse, pommes, arene, couleur, truc, sortie


#def clic_pause(x, y):
#    xclic, yclic = attend_clic_gauche()
#    if yclic > y and yclic < y + 37:
#        if xclic > x - 37 and xclic < x:
#            return True
#        else:
#            False
#    elif xclic and yclic == None:
#        return False    
#     
#    
#def affiche_menu_pause(x, y):
#    efface_tout()
#    a = y / 8
#    image(x/2, y/2, 'backmenu.gif', ancrage = 'center')
#    texte(x / 2, y / 2, 'PAUSE', ancrage = 'center', 
#          couleur = 'yellow', taille = 50 )
#    texte(x / 2, 7.5 * a , 'REPRENDRE', ancrage = 'center', 
#          couleur = 'yellow', taille = 20) 
#    mise_a_jour()
        
    
def game_over(x, y, evenement):
    '''
    affiche une page de game over centrée après que la partie a été perdue
    
    prend comme paramètres les dimensions en pixel de la fenêtre (x et y) et 
    la manière dont le serpent a perdu (evenement)
    renvoie les coordonnées des trois boutons 'Rejouer', 'Options' et 'Quitter'
    '''
    efface_tout()
    image(x/2, y/2, 'backmenu.gif', ancrage = 'center')
    bx = x_fenetre / 6
    by = y_fenetre / 1.5

    texte(3 * bx, by - by / 2, "GAME OVER", couleur="green", 
          ancrage="center", police="Helvetica", taille=40)
    attente(1)
    texte(3 * bx, by - by / 3, str(evenement), couleur="green", 
          ancrage="center", police="Helvetica", taille=20)
    attente(1)
    texte(3 * bx, y / 2, "Score: "+str(score), couleur="green", 
          ancrage="center", police="Helvetica", taille=30)
    
    #bouton 'Jouer'
    texte(1.5 * bx, by + bx / 4, 'Rejouer', ancrage = 'center', 
          couleur = 'yellow')
    
    # bouton 'Paramètres'
    texte(3 * bx, by + bx / 4, ' ', ancrage = 'center', 
          couleur = 'yellow')
    
    # bouton 'Quitter'
    texte(4.5 * bx, by + bx / 4, 'Quitter', ancrage = 'center', 
          couleur = 'yellow')
    
    return bx, 2 * bx, 2.5 * bx, 3.5 * bx, 4 * bx, 5 * bx, by, by + bx / 2


def fonction_ecran_titre(j1, j2, p1, p2, q1, q2, y, Y):
    '''
    prend en paramètre une série de coordonnnées permettant de définir la 
    position des boutons de l'écran titre
    renvoie un triplet de booléens dont un seul est True, permettant de 
    savoir à quel écran passer après le clic 
    (écran de jeu, d'options ou toujours écran titre)
    '''
    (Abs, Ord) = attend_clic_gauche()
    if Ord < Y and Ord > y:            
        if Abs > j1 and Abs < j2:
            return True, False, False
        if Abs > p1 and Abs < p2:
            return False, True, False
        if Abs > q1 and Abs < q2:
            return False, False, True
        
    ev = attend_ev()
    if type_ev(ev) == 'Quitte':
        return False, False, True

    


def case_vers_pixel(case):
    """
	Fonction recevant les coordonnées d'une case du plateau sous la 
	forme d'un couple d'entiers (ligne, colonne) et renvoyant les 
	coordonnées du pixel se trouvant au centre de cette case. Ce calcul 
	prend en compte la taille de chaque case, donnée par la variable 
	globale taille_case.
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case
    
              
def nouvel_objet(lst, f, serpent):
    '''
    gère l'apparition aléatoire d'un objet (pomme, mur ou missile)
    prend en paramètre la liste concernée, une fréquence d'apparition 
    et le serpent (afin d'éviter que l'objet ne soit créé sur lui)
    '''
    np = randint(1, int(1 / f))
    if np == 1:
        xp = randint(0, largeur_plateau - 1)
        yp = randint(0, hauteur_plateau - 1)
        if (xp, yp) not in serpent:
            lst += [(xp, yp)]
    
    
def affiche_pommes(pommes):
    for pomme in pommes:
        x, y = case_vers_pixel(pomme)
        image(x, y, 'petitepomme.gif', ancrage='center', tag='pomme')
        rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7, 
                  couleur='darkgreen', remplissage='darkgreen')
                  
                  
def couleur_aleatoire():
    # sélection de couleurs pour le serpent multicolore
    return choice(['purple', 'darkblue', 'blue', 'darkgreen', 'green', 
                   'yellow', 'orange', 'red', 'pink'])


def affiche_serpent(serpent, couleur):
    x, y = case_vers_pixel(serpent[0])
    cercle(x, y, taille_case/2 + 1, couleur = 'black', 
           remplissage = 'black', tag = 'tete')
    
    sc = list(serpent)
    sc.pop(0)
    n = 1
    tag_srpt = ['tete']
    
    if couleur == 'multicolore':
        for s in sc:
            x, y = case_vers_pixel(s)
            cercle(x, y, taille_case/2 + 1, couleur = 'black', 
                   remplissage = couleur_aleatoire(), tag = 'boule' + str(n))
            tag_srpt += 'boule' + str(n)
            n += 1
    else:
        for s in sc:
            x, y = case_vers_pixel(s)
            cercle(x, y, taille_case/2 + 1, couleur = 'black', 
                   remplissage = couleur, tag = 'boule' + str(n))
            tag_srpt += 'boule' + str(n)
            n += 1
    
    return tag_srpt
    
            
def cache_serpent(lst, n):
    '''
    utile seulement dans le cas de l'arène infinie
    sert à éviter que le serpent ne voit sa queue disparaître 
    devant lui comme dans une arène torique
    
    prend en paramètres une liste (le serpent) et un nombre 
    de case à ne pas afficher (la queue du serpent)
    '''
    l = list(lst)
    for i in range(n):
        l.pop()
    return l
        
        
def affiche_murs(murs):
    for mur in murs:
        x, y = case_vers_pixel(mur)
        image(x, y, 'obstacle0.gif', tag='mur')
        
        
def affiche_tetes(tetes):
    for missile in tetes:
        x, y = case_vers_pixel(missile)
        cercle(x, y, taille_case/2, remplissage='blue')
        rectangle(x - 2, y - taille_case * .4, x + 2, y - taille_case * .7, 
                  remplissage='black')
        rectangle(x - 2, y + taille_case * .4, x + 2, y + taille_case * .7, 
                  remplissage='black')
        
        
def change_direction(direction, touche, l):
    '''
    gère le changement de direction du serpent
    
    prend comme paramètres la direction actuelle du serpent (dans le cas où 
    elle ne serait pas modifiée), la touche pressée et la longeur du serpent
    renvoie la nouvelle direction
    
    >>> change_direction((1, 0), 'Left', 2)
    (1, 0)
    >>> change_direction((1, 0), 'Left', 1)
    (-1, 0)
    '''
    xd, yd = direction 
    x, y = 0, 0
    if touche == 'Up':
         x, y = 0, -1
    elif touche == 'Down':
        x, y = 0, 1
    elif touche == 'Right':
        x, y = 1, 0
    elif touche == 'Left':
         x, y = -1, 0
    else:
        return direction
    if xd + x == 0 and yd + y == 0 and l > 1:
        return direction
    else: 
        return x, y
    

def tetes_chercheuses(tetes, dir_tetes):
    '''
    gère le déplacement et le changement de direction aléatoire des missiles
    
    prend comme paramètres la liste de missiles et la liste de leurs direction 
    respectives
    renvoie deux nouvelles listes contenant les positions/directions 
    des missiles au tour suivant
    '''
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    av_t = list(tetes)
    av_dir = list(dir_tetes)
    
    for missile in range(len(tetes)):
        xt, yt = tetes[missile]
        av_t.remove((xt, yt))
        
        n = randint(1, 5)
        x, y = dir_tetes[missile]
        if n == 1:
            xd, yd = choice(directions)
            if x + xd != 0 and y + xd != 0:
                xd, yd = x, y
        else:
            xd, yd = x, y
            
        xt += xd
        yt += yd
        av_t += [(xt, yt)]
        av_dir += [(xd, yd)]
        
    return av_t, av_dir
                  
                  
def avance_serpent(serpent, direction, pommes):
    '''
    gère le déplacement du serpent
    
    prend comme paramètres le serpent, sa direction et la position des pommes
    renvoie le serpent du tour suivant
    
    >>> avance_serpent([(0, 0)], (0, 1), [])
    [(0, 1)]
    
    >>> avance_serpent([(0, 0)], [0, 1], [(0, 1)])
    [(0, 1), (0, 0)]
    
    >>> avance_serpent([(0, 0), (0, 1)], [1, 0], [])
    [(1, 0), (0, 0)]
    '''
    xs, ys = serpent[0]
    xd, yd = direction
    xs += xd
    ys += yd
    if (xs, ys) not in pommes:
        serpent.pop()
    return [(xs, ys)] + serpent
        

#def avance_infini(serpent, direction):
#    '''
#    gère le déplacement du serpent dans le mode deux joueurs
#    '''
#    xs, ys = serpent[0]
#    xd, yd = direction
#    xs += xd
#    ys += yd
#    return [(xs, ys)] + serpent
    

def sortie_ecran(objet):
    '''
    détermine si un objet (en paramètre) sort de la fenêtre
    renvoie True si c'est le cas et False sinon 
    '''
    x, y = objet
    if x < 0 or y < 0 or y > hauteur_plateau - 1 or x > largeur_plateau - 1:
        return True
    else:
        return False

    
def collision(serpent):
    '''
    détermine si le serpent se mange lui-même
    renvoie True si c'est le cas et False sinon
    '''
    sc = list(serpent)
    sc.pop(0)
    if serpent[0] in sc:
        return True 
    else:
        return False
       
        
def collision_ext(serpent, murs, tetes):
    ''' 
    détermine si le serpent entre en collision avec un mur ou un missile
    renvoie True si c'est le cas et False sinon
    '''
    sc = list(serpent)
    sc.pop(0)
    x = 0 
    if serpent[0] in murs:
        x += 1
        
    for s in serpent:
        if s in tetes:
            x += 1
            
    if x != 0:
        return True 
    else:
        return False
        
        
def arene_torique(serpent):
    '''
    si l'arène est torique:
    prend en argument le serpent (une liste)
    
    détermine s'il sort de l'écran et le fait réapparaître de l'autre côté 
    (le cas échéant)
    renvoie également xMap et yMap, qui indiquent de quel côté 
    le serpent est sorti
    '''
    nv_s = []
    xMap, yMap = serpent[0]
    xMap = xMap // largeur_plateau
    yMap = yMap // hauteur_plateau
        
    for s in serpent:
        x, y = s
        
        x = x % largeur_plateau
        y = y % hauteur_plateau
        
        nv_s += [(x, y)]
        
    return nv_s, xMap, yMap
                  
              
if __name__ == "__main__":                 
    cree_fenetre(x_fenetre, y_fenetre + 37)  
        
    ecran_titre, jouer, quitte = True, False, False
    (framerate, pommes_multiples, torique, openworld, couleur, obstacles, 
    bombes) = init_param()
    
    while not jouer:
      
        j1, j2, p1, p2, q1, q2, y, Y = affiche_ecran_titre(x_fenetre, 
                                                           y_fenetre)
        jouer, options, quitte = fonction_ecran_titre(j1, j2, p1, p2, q1, q2, 
                                                      y, Y)
        
        if quitte:
            ferme_fenetre()
            
        if options:
            ecran_titre = False
            vitesse, pommes, arene, couleur, truc = init_menu()
            while ecran_titre == False: 
                vitesse, pommes, arene, couleur, truc, sortie = menu_option(
                        x_fenetre, y_fenetre, "MENU", vitesse, 
                            pommes, arene, couleur, truc)
                ecran_titre = sortie
                
            (framerate, pommes_multiples, torique, openworld, couleur, 
            obstacles, bombes) = renvoi_parametres(x_fenetre, y_fenetre, 
                                                  "MENU", vitesse, pommes, 
                                                  arene, couleur, truc)
            
    sortie_definitive = False # l'utilisateur ne ferme pas définitivement 
                                 # le programme

    # lancement du jeu
    while not sortie_definitive:
        
        carte = 'Background_4.png'
        deux_joueurs = False
        direction = (0, 0)  # direction initiale du serpent
        pommes = [(randint(0, largeur_plateau - 1), 
                   randint(0, hauteur_plateau - 1))] # liste des coordonnées 
                                              # des cases contenant des pommes
        serpent = [(largeur_plateau / 2, 
                    hauteur_plateau / 2)] # liste des coordonnées de cases 
                                             # adjacentes décrivant le serpent
        murs = []
        tetes = []      # coordonnées des tetes chercheuses
        dir_tetes = []
        G = 0
        
        jouer = True
        while jouer: #début de la partie
            # affichage des objets
            efface_tout()
            r = randint(1, 1000)
            if r == 1:
                image(x_fenetre / 2, y_fenetre / 2, 'backmenu.gif', 
                      ancrage = 'center')
                image(x_fenetre / 2, y_fenetre / 2, 'sprite_43.png', 
                      ancrage = 'center')
                texte(x_fenetre / 2, y_fenetre / 4, 
                      'Merci de jouer à', ancrage = 'center')
                texte(x_fenetre / 2, 3 * y_fenetre / 4, 
                      'par Loris & Lysandre', ancrage = 'center')
            else:
                image(x_fenetre / 2, y_fenetre / 2, carte, 
                      ancrage='center')
            rectangle(0, y_fenetre, x_fenetre, y_fenetre + 37, 
                      remplissage = 'black')
            score = len(serpent) - 1
            texte(0, y_fenetre + 37, ' Score :' + str(score), 
                  couleur='green', ancrage='sw', police='Helvetica')
            # texte(x_fenetre, y_fenetre + 37, 'II ', couleur = 'green', 
                  # ancrage = 'se')
            affiche_pommes(pommes) 
            l = cache_serpent(serpent, G)  # pour l'arène infinie
            affiche_serpent(l, couleur)
            affiche_murs(murs)
            affiche_tetes(tetes)
            
            mise_a_jour()
            
            # gestion des événements
            ev = donne_ev()
            ty = type_ev(ev)
            if ty == 'Quitte':
                ferme_fenetre()
            #elif clic_pause() == True:
             #   affiche_ecran_pausee(x_fenetre, y_fenetre)
              #  while not clic_choix_parametre_sortie(x, y, xclic, yclic):
                #    pass
            elif ty == 'Touche':
                direction = change_direction(direction, touche(ev), 
                                             len(serpent))
                
            serpent = avance_serpent(serpent, direction, pommes)
            tetes, dir_tetes = tetes_chercheuses(tetes, dir_tetes)
            
            if collision_ext(serpent, murs, tetes):
                jouer = False
                evenement = "Le serpent s'est cogné"
                
            if collision(serpent):
                jouer = False
                evenement = "Le serpent s'est mangé"
                
            if torique:
                serpent, xMap_1, yMap_1 = arene_torique(serpent)
                if tetes:
                    tetes, xMap_t, yMap_t = arene_torique(tetes)
            
            elif openworld:
                serpent, xMap_1, yMap_1 = arene_torique(serpent)
                for t in tetes:
                    if sortie_ecran(t):
                        tetes.remove(t)
                if xMap_1 != 0 or yMap_1 != 0:
                    G = len(serpent) 
                    n = randint(1, 5)
                    carte = 'Background_' + str(n) + '.png'
                    for p in pommes:
                        pommes.remove(p)
                        n = randint(1, 4)
                        if len(pommes) < 5 or n == 1:
                            pommes += [(randint(0, largeur_plateau - 1), 
                                        randint(0, hauteur_plateau - 1))]
                    for m in murs:
                        murs.remove(m)
                        n = randint(1, 4)
                        if len(murs) < 5 or n == 1:
                            murs += [(randint(0, largeur_plateau - 1), 
                                      randint(0, hauteur_plateau - 1))]
            else:
                if sortie_ecran(serpent[0]):
                    jouer = False
                    evenement = "Le serpent est sorti de l'écran"
                    
            # nouvelle pomme
            if pommes_multiples:
                fp = 1 / (40 + score / 3)   # fréquence moyenne d'apparition 
                nouvel_objet(pommes, fp, serpent)  # des pommes
            else:
                if pommes == []:
                    pommes += [(randint(0, largeur_plateau - 1), 
                                randint(0, hauteur_plateau - 1))]
                    
            for p in pommes:
                if p in serpent or p in tetes or p in murs:
                    pommes.remove(p)
        
            # apparition de murs 
            if score > 5 and obstacles:
                fm = 1 / (score * 6 + 1 / 50)  # fréquence moyenne d'apparition
                nouvel_objet(murs, fm, serpent)  # des murs
                
                for m in murs:
                    if m in tetes:
                        murs.remove(m)
                        
            # apparition des têtes chercheuses
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if score > 10 and bombes:
                ft = 1 / (score * 6 + 1 / 160) 
                nouvel_objet(tetes, ft, serpent)
                dir_tetes += [choice(directions)]
                        
                for l in range(len(tetes)):
                    xd, yd = dir_tetes[l]
                    x, y = tetes[l]
                    t = x + xd, y + yd
                    if t in murs or t in pommes or t in tetes:
                        tetes.remove(tetes[l])
                        dir_tetes.remove(dir_tetes[l])  
            if G != 0:
                G -= 1 
            # attente avant rafraîchissement
            sleep(1/(framerate + score / 2))
            
        menu, sortie_definitive, quitte = True, False, False
        j1, j2, p1, p2, q1, q2, y, Y = game_over(x_fenetre, y_fenetre + 37, 
                                                 evenement)
        while menu:
            jouer, options, quitte = fonction_ecran_titre(j1, j2, p1, p2, q1, 
                                                          q2, y, Y)
            if jouer:
                menu = False
                
            if options:
                menu = False
                ecran_titre = False
                vitesse, pommes, arene, couleur, truc = init_menu()
                while ecran_titre == False : 
                    vitesse, pommes, arene, couleur, truc, 
                    sortie = menu_option(
                            x_fenetre, y_fenetre, 
                            "Bravo ! Vous avez trouver un easter egg:" + 
                            "le menu qui ne fonctionne pas", 
                                         vitesse, pommes, arene, couleur, truc)
                    ecran_titre = sortie
                (framerate, pommes_multiples, torique, openworld, couleur, 
                obstacles, bombes) = renvoi_parametres(x_fenetre, y_fenetre, 
                                                      "REJOUER", vitesse, 
                                                      pommes, arene, couleur, 
                                                      truc)
            if quitte == True:
                menu = False
                sortie_definitive = True
                
    ferme_fenetre()
    
testmod()