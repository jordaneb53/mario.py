import pygame

pygame.init()

# Initialisation de l'écran
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption("Jeu avec plateformes, gravité et saut")

# Chargement des images de fond et de personnage
try:
    fond = pygame.image.load("C:/Users/stagiaire/Desktop/jordane/projets/Mario.py/options/image.png/background.png").convert()
except pygame.error:
    print("Erreur : le fichier background.png est introuvable.")
    pygame.quit()
    exit()

try:
    personnage_droite = pygame.image.load("C:/Users/stagiaire/Desktop/jordane/projets/Mario.py/options/image.png/mario.png").convert_alpha()
    personnage_gauche = pygame.transform.flip(personnage_droite, True, False)  
except pygame.error:
    print("Erreur : le fichier mario.png est introuvable.")
    pygame.quit()
    exit()

# Paramètres du personnage et du saut
personnage = personnage_droite
personnage_x = 100
personnage_y = 500
vitesse = 1          
gravite = 0.2      # Gravité plus faible pour un saut plus lent
vitesse_y = 0        
saut_force = 10      # Force de saut ajustée pour un saut plus lent
au_sol = False       
saut_autorise = True  

# Création des plateformes
plateformes = [
    pygame.Rect(200, 600, 200, 20),
    pygame.Rect(500, 500, 300, 20),
    pygame.Rect(900, 400, 200, 20),
]

# Boucle principale du jeu
running = True
while running:
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and au_sol and saut_autorise:  
                vitesse_y = -saut_force  
                au_sol = False          
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                saut_autorise = True   # Réautoriser le saut lorsque la barre d'espace est relâchée

    # Gestion du déplacement et changement d'image selon la direction
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:  
        personnage_x -= vitesse
        personnage = personnage_gauche
    elif touches[pygame.K_RIGHT]:  
        personnage_x += vitesse
        personnage = personnage_droite

    # Application de la gravité lorsque le personnage est en l'air
    if not au_sol:
        vitesse_y += gravite  
    personnage_y += vitesse_y 

    # Détection des collisions avec les plateformes
    au_sol = False  
    personnage_rect = pygame.Rect(personnage_x, personnage_y, personnage.get_width(), personnage.get_height())
    for plateforme in plateformes:
        if personnage_rect.colliderect(plateforme) and vitesse_y >= 0:
            personnage_y = plateforme.top - personnage.get_height() 
            vitesse_y = 0  
            au_sol = True  
            break

    # Empêcher le personnage de tomber sous l'écran
    if personnage_y > screen.get_height() - personnage.get_height():
        personnage_y = screen.get_height() - personnage.get_height()
        vitesse_y = 0
        au_sol = True

    # Affichage du fond et des plateformes
    screen.blit(fond, (0, 0)) 
    for plateforme in plateformes:
        pygame.draw.rect(screen, (0, 128, 0), plateforme)  
    
    # Affichage du personnage
    screen.blit(personnage, (personnage_x, personnage_y))  

    # Mise à jour de l'affichage
    pygame.display.flip()

pygame.quit()
