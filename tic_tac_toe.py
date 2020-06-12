import pygame
import sys


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
    # fonction pour l'affichage
    def afficher(self):
        for ligne in self.lignes:
            pygame.draw.line(self.ecran, (0,0,0),ligne[0], ligne[1], 2)

    def affiche_grilles(self):
        print(self.grille)

    # fixer les valeurs
    def fixer_la_valeur(self, x, y, valeur):
        self.grille[y][x] = valeur





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


    def f_principale(self):
        while self.jeu_encours:
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
                    self.grille.fixer_la_valeur(position_x, position_y, 'x')
                    # condition si le compteur est pair ou impair
                    if self.compteur % 2 == 0:
                        self.grille.fixer_la_valeur(position_x, position_y, self.player_x)
                    else:
                        self.grille.fixer_la_valeur(position_x, position_y, self.player_O)
                    self.compteur += 1
                self.grille.affiche_grilles()
            self.ecran.fill((249, 249,240))
            self.grille.afficher()

            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    Jeu().f_principale()
    pygame.QUIT()