import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définition des constantes
TAILLE_ECRAN = (288, 512)
COULEUR_FOND = (135, 206, 235)
COULEUR_OISEAU = (255, 255, 255)
COULEUR_TUYAU = (0, 255, 0)
COULEUR_SOL = (255, 0, 0)
COULEUR_SCORE = (255, 255, 255)

# Création de la fenêtre
fenetre = pygame.display.set_mode(TAILLE_ECRAN)

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

# Création du score
score = 0
font_score = pygame.font.SysFont("Arial", 24)

# Création des niveaux
niveaux = [
    {"tuyau_hauteur": 200, "tuyau_vitesse_x": -2},
    {"tuyau_hauteur": 250, "tuyau_vitesse_x": -3},
    {"tuyau_hauteur": 300, "tuyau_vitesse_x": -4},
]


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
        tuyau_y = random.randint(100, 300)
        score += 1

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
    pygame.draw.rect(fenetre, COULEUR_OISEAU, (oiseau_x, oiseau_y, oiseau_largeur, oiseau_hauteur))
    pygame.draw.rect(fenetre, COULEUR_TUYAU, (tuyau_x, tuyau_y, tuyau_largeur, tuyau_hauteur))
    pygame.draw.rect(fenetre, COULEUR_SOL, (sol_x, sol_y, sol_largeur, sol_hauteur))

    # Affichage du score
    score_text = font_score.render(str(score), True, COULEUR_SCORE)
    fenetre.blit(score_text, (10, 10))

    # Mise à jour de la fenêtre
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    # Changement de niveau
    if score >= 10:
        tuyau_hauteur = niveaux[1]["tuyau_hauteur"]
        tuyau_vitesse_x = niveaux[1]["tuyau_vitesse_x"]
    elif score >= 20:
        tuyau_hauteur = niveaux[2]["tuyau_hauteur"]
        tuyau_vitesse_x = niveaux[2]["tuyau_vitesse_x"]