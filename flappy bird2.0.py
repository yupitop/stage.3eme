import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des constantes
TAILLE_ECRAN = (288, 512)
COULEUR_FOND = (135, 206, 235)

# Création de la fenêtre
fenetre = pygame.display.set_mode(TAILLE_ECRAN)

# Chargement des images
oiseau_image = pygame.image.load("oiseau.png")
oiseau_image = pygame.transform.scale(oiseau_image, (20, 20))

tuyau_image = pygame.image.load("tuyau.png")
tuyau_image = pygame.transform.scale(tuyau_image, (50, 200))

sol_image = pygame.image.load("sol.png")
sol_image = pygame.transform.scale(sol_image, (288, 50))

# Création de l'oiseau
oiseau_x = 50
oiseau_y = 200
oiseau_largeur = 20
oiseau_hauteur = 20
oiseau_vitesse_y = 0

# Création des tuyaux
tuyau_x = 300
tuyau_y = 200
tuyau_largeur = 50
tuyau_hauteur = 200
tuyau_vitesse_x = -2

# Création du sol
sol_x = 0
sol_y = 450
sol_largeur = 288
sol_hauteur = 50

# Boucle principale
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                oiseau_vitesse_y = -5

    # Déplacement de l'oiseau
    oiseau_y += oiseau_vitesse_y
    oiseau_vitesse_y += 0.2

    # Déplacement des tuyaux
    tuyau_x += tuyau_vitesse_x
    if tuyau_x < -50:
        tuyau_x = 300
        tuyau_y = 200

    # Collision avec les tuyaux
    if (oiseau_x + oiseau_largeur > tuyau_x and
        oiseau_x < tuyau_x + tuyau_largeur and
        oiseau_y < tuyau_y + tuyau_hauteur and
        oiseau_y + oiseau_hauteur > tuyau_y):
        print("Game over")
        pygame.quit()
        sys.exit()

    # Collision avec le sol
    if oiseau_y + oiseau_hauteur > sol_y:
        print("Game over")
        pygame.quit()
        sys.exit()

    # Dessin de la fenêtre
    fenetre.fill(COULEUR_FOND)
    fenetre.blit(oiseau_image, (oiseau_x, oiseau_y))
    fenetre.blit(tuyau_image, (tuyau_x, tuyau_y))
    fenetre.blit(sol_image, (sol_x, sol_y))

    # Mise à jour de la fenêtre
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
