import pygame
import sys

# Alapvető beállítások
pygame.init()
szelesseg, magassag = 800, 600
feher = (255, 255, 255)
fekete = (0, 0, 0)

# Ablak beállítása
ablak = pygame.display.set_mode((szelesseg, magassag))
pygame.display.set_caption("Pong Játék")

# Ütők és labda beállítása
uto_szelesseg, uto_magassag = 10, 100
bal_uto = pygame.Rect(30, magassag // 2 - uto_magassag // 2, uto_szelesseg, uto_magassag)
jobb_uto = pygame.Rect(szelesseg - 40, magassag // 2 - uto_magassag // 2, uto_szelesseg, uto_magassag)
labda = pygame.Rect(szelesseg // 2 - 15, magassag // 2 - 15, 30, 30)

# Mozgási sebességek
labda_sebesseg_x, labda_sebesseg_y = 7, 7
uto_sebesseg = 10

# Pontszámok
bal_pont, jobb_pont = 0, 0
font = pygame.font.Font(None, 74)

# Játék ciklus
while True:
    for esemeny in pygame.event.get():
        if esemeny.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Billentyűzet input
    billentyuk = pygame.key.get_pressed()
    if billentyuk[pygame.K_w] and bal_uto.top > 0:
        bal_uto.y -= uto_sebesseg
    if billentyuk[pygame.K_s] and bal_uto.bottom < magassag:
        bal_uto.y += uto_sebesseg
    if billentyuk[pygame.K_UP] and jobb_uto.top > 0:
        jobb_uto.y -= uto_sebesseg
    if billentyuk[pygame.K_DOWN] and jobb_uto.bottom < magassag:
        jobb_uto.y += uto_sebesseg

    # Labda mozgása
    labda.x += labda_sebesseg_x
    labda.y += labda_sebesseg_y

    # Labda falhoz ér
    if labda.top <= 0 or labda.bottom >= magassag:
        labda_sebesseg_y *= -1

    # Labda ütközés az ütőkkel
    if labda.colliderect(bal_uto) or labda.colliderect(jobb_uto):
        labda_sebesseg_x *= -1

    # Pontszerzés
    if labda.left <= 0:
        jobb_pont += 1
        labda.x, labda.y = szelesseg // 2 - 15, magassag // 2 - 15
        labda_sebesseg_x *= -1
    if labda.right >= szelesseg:
        bal_pont += 1
        labda.x, labda.y = szelesseg // 2 - 15, magassag // 2 - 15
        labda_sebesseg_x *= -1

    # Játék felület frissítése
    ablak.fill(fekete)
    pygame.draw.rect(ablak, feher, bal_uto)
    pygame.draw.rect(ablak, feher, jobb_uto)
    pygame.draw.ellipse(ablak, feher, labda)
    pygame.draw.aaline(ablak, feher, (szelesseg // 2, 0), (szelesseg // 2, magassag))

    # Pontok kirajzolása
    bal_szoveg = font.render(str(bal_pont), True, feher)
    jobb_szoveg = font.render(str(jobb_pont), True, feher)
    ablak.blit(bal_szoveg, (szelesseg // 4, 20))
    ablak.blit(jobb_szoveg, (szelesseg * 3 // 4, 20))

    pygame.display.flip()
    pygame.time.delay(30)
