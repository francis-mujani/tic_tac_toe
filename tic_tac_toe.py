import pygame
import sys

################################# CLASS GRILLES #####################################"
class Grilles :
    def __init__(self, ecran):
        self.ecran = ecran
        # parametres de la ligne
        self.lignes = [((200, 0), (200, 600)), # point de depart de la ligne (200, 0)ç et le point final (200, 600)
                       ((400, 0), (400, 600)),
                       ((0, 200), (600,200)),
                       ((0, 400), (600, 400))]
        # Initialisation de la grille
        self.grille = [[None for x in range(0,3)] for y in range(0,3)]
        # Initialisation de la variable pour verifier si le compteur est 'ON'
        self.compteur_on = False

    # fonction pour l'affichage
    def afficher(self):
        for ligne in self.lignes:
            pygame.draw.line(self.ecran, (0,0,0),ligne[0], ligne[1], 2)
        # Affiche les x et o
        for y in range(0, len(self.grille)): # loupe a travert chaque ligne
            for x in range(0, len(self.grille)): # on loupe a travert chaque colonnes
                if self.grille[y][x] == 'X': # une case prise dans la grille
                    pygame.draw.line(self.ecran, (0,0,0),(x*200, y*200), (200 + (x*200),200 + (y*200)), 3)
                    pygame.draw.line(self.ecran, (0, 0, 0),((x * 200),200+(y * 200)),(200 + (x * 200),(y * 200)),3)
                elif self.grille[y][x] == 'O':
                    pygame.draw.circle(self.ecran, (0,0,0), (100 + (x*200), 100+(y*200)), 80,3)

    def affiche_grilles(self):
        print(self.grille)

    # fixer les valeurs
    def fixer_la_valeur(self, x, y, valeur):
        #self.grille[y][x] = valeur
        # condition si une case possede la valeur None
        if self.grille[y][x] == None :
            # si une case possede de la valeur None, on va consideré que compteur_on egale a True
            self.grille[y][x] = valeur
            self.compteur_on = True

    # fonction qui fixe la valeur de case en NONE
    def fixer_none(self, ligne, colonne, valeur):
        self.grille[ligne][colonne] = valeur

###################################### CLASS JEU #####################################

class Jeu :
    def __init__(self):

        self.ecran = pygame.display.set_mode((600,600))
        pygame.display.set_caption('Tic Tac Toe')
        self.jeu_encours = True
        self.grille = Grilles(self.ecran)

        # initialisation des variables x et 0
        self.player_x = 'X'
        self.player_O = 'O'
        # initialisation du compteur
        self.compteur = 0
        # initialisation de la variable ecran
        self.ecran_debut = True


    def f_principale(self):
        while self.jeu_encours:
            # la boucle pour ecran du debut
            while self.ecran_debut:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.ecran_debut = False
                self.ecran.fill((230, 230, 230))
                # geré les messages du debut du jeu
                self.creer_message('grande', 'Tic Tac Toe', (0,0,0), [200, 30, 200, 50])
                self.creer_message('petite', "Ce jeu se joue à deux et chaqu'un se verra attribuer un symbole",
                                   (0,0,0), [90, 130, 400, 50])
                self.creer_message('petite', 'X ou O', (0,0,0), [270, 150, 100, 100])
                self.creer_message('petite', 'Le premier joueur qui reussi à aligner 3 de ses symboles gagne',
                                   (0,0,0), [90, 170, 200, 50])
                self.creer_message('moyenne', 'Pour commencer le jeu, appuyer sur Entre',
                                   (0, 0, 0), [90, 350, 200, 50])
                self.creer_message('moyenne', 'Appuyer sur espace pour recommencer la partie',
                                   (0, 0, 0), [70, 400, 200, 50])
                self.creer_message('moyenne', 'Pour revenir a cette scran, appuyer sur ESC',
                                   (0, 0, 0), [90, 450, 200, 50])
                self.creer_message('petite', 'Create by Francis Mujani', (0, 0, 0), [230, 530, 250, 50])
                self.creer_message('petite', '06-52-64-91-81', (0, 0, 0), [270, 550, 250, 50])
                pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # ajouter l'evenement qui correspond au clique droit
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    # obtenir la position de la souris
                    position = pygame.mouse.get_pos()
                    print(position)
                    # on crée un systeme d'indexation, chaque grille doit avoir sa propre valeur (index)
                    position_x, position_y = position[0]//200 , position[1]//200
                    print(position_x, position_y)

                    # declaration de la fonction (pour afficher les valeurs )
                    print(self.compteur, self.compteur%2)
                    #self.grille.fixer_la_valeur(position_x, position_y, 'x')
                    # condition si le compteur est pair ou impair
                    if self.compteur % 2 == 0:
                        self.grille.fixer_la_valeur(position_x, position_y, self.player_x)
                    else:
                        self.grille.fixer_la_valeur(position_x, position_y, self.player_O)

                    if self.grille.compteur_on:
                        self.compteur +=1
                        self.grille.compteur_on = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.recommencer()
                    if event.key == pygame.K_SPACE:
                        self.ecran_debut = True

            liste_x = []
            liste_o = []
            liste_lignes_x = []
            liste_colonnes_x = []
            liste_lignes_o = []
            liste_colonnes_o = []

            print(self.compteur)
            self.grille.affiche_grilles()
            self.ecran.fill((249, 249, 240))
            self.grille.afficher()

            pygame.display.flip()

    # fonction qui cherche si un joueur gagne
    #def gagnant(self, liste_x, liste_o, liste_colonnes_x, liste_lignes_x, liste_lignes_o, liste_colonnes_o):

            for ligne in range(0, len(self.grille.grille)):
                for colonne in range(0, len(self.grille.grille)):
                    if self.grille.grille[ligne][colonne] == 'X': # cette condition est vraie lorsque une case a la valeur x
                        x_position = (ligne,colonne)
                        liste_x.append(x_position)
                    elif self.grille.grille[ligne][colonne] == 'O': # cette condition est vraie lorsque une case a la valeur x
                        o_position = (ligne,colonne)
                        liste_o.append(o_position)
            if len(liste_x) >= 3:
                for (ligne, colonne) in liste_x:
                    liste_lignes_x.append(ligne)
                    liste_colonnes_x.append(colonne)
                # ici le count methode va compter le nombre de zero qui y'a dans cette liste et si y'en a 3, ce que le x a gagné
                if liste_lignes_x.count(0) == 3 or liste_lignes_x.count(1) == 3 or liste_lignes_x.count(1) == 3:
                    print('X GAGNE')
                if liste_colonnes_x.count(0) == 3 or liste_colonnes_x.count(1) == 3 or liste_colonnes_x.count(2) == 3:
                    print('X GAGNE')

                # verifier si le joueur a gagné en diagonale
                if liste_lignes_x == liste_colonnes_x or liste_lignes_x ==liste_colonnes_x[::-1]:
                    print('X GAGNE')
                #print(liste_lignes_x, liste_colonnes_x)

            if len(liste_o) >= 3:
                for (ligne, colonne) in liste_o:
                    liste_lignes_o.append(ligne)
                    liste_colonnes_o.append(colonne)
                # ici le count methode va compter le nombre de zero qui y'a dans cette liste et si y'en a 3, ce que le x a gagné
                if liste_lignes_o.count(0) == 3 or liste_lignes_o.count(1) == 3 or liste_lignes_o.count(1) == 3:
                    print('O GAGNE')
                if liste_colonnes_o.count(0) == 3 or liste_colonnes_o.count(1) == 3 or liste_colonnes_o.count(2) == 3:
                    print('O GAGNE')

                # verifier si le joueur a gagné en diagonale
                if liste_lignes_o == liste_colonnes_o or liste_lignes_x ==liste_colonnes_o[::-1]:
                    print('O GAGNE')


    # fonction qui attribue la valeur None a chaque des cases
    def recommencer(self):
        for ligne in range(0, len(self.grille.grille)):
            for colonne in range(0, len(self.grille.grille)):
                self.grille.fixer_none(ligne, colonne, None)

    # fonction qui affiche les messages
    def creer_message(self,font, message, couleur, message_rectangle):
        if font == 'petite':
            font = pygame.font.SysFont('Lato', 20, False)
        if font == 'moyenne':
            font = pygame.font.SysFont('Lato', 30, False)
        elif font == 'grande':
            font = pygame.font.SysFont('Lato', 40, True)
        message = font.render(message, True, couleur)

        self.ecran.blit(message, message_rectangle)

if __name__ == '__main__':
    pygame.init()
    Jeu().f_principale()
    pygame.QUIT()