import pygame
import random
pygame.init()

screen = pygame.display.set_mode((640,690))
pygame.display.set_caption("Feed Chick")
clock = pygame.time.Clock()

score = 0
myFont = pygame.font.SysFont("arialblack",32)
myFont2 = pygame.font.SysFont("arialblack",96)
myScore = myFont.render(f"Score: {score}", True, (222,222,222))
scorePosition = myScore.get_rect(topleft=[240,635])


monsterImg = pygame.image.load("monster 24.png")
monsterPosition = monsterImg.get_rect(topleft=(320,320))

breadImg = pygame.image.load("bread 24.png")

collectBread = pygame.mixer.Sound("blip-131856.mp3")
levelUp = pygame.mixer.Sound("power-up-sparkle-1-177983.mp3")
winner = pygame.mixer.Sound("you-win-sequence-1-183948.mp3")

def placeBread():
    while True:
        breadPosition = pygame.Rect((random.randint(0, wall)), (random.randint(0, wall)),
                                    breadImg.get_width(), breadImg.get_height())
        if breadPosition.colliderect(monsterPosition):
            continue
        return breadPosition

def youWin():
    global running
    text = myFont2.render("You win", True, (45,189,61))
    textPosition = text.get_rect(center=(320,320))
    screen.blit(text,textPosition)
    pygame.display.update()
    winner.play()
    pygame.time.wait(3500)
    running = False


wall =616
breadPosition = placeBread()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and monsterPosition.y > 0:
        monsterPosition.y -= 5
    elif keys[pygame.K_a] and monsterPosition.x > 0:
        monsterPosition.x -= 5
    elif keys[pygame.K_s] and monsterPosition.y < wall:
        monsterPosition.y += 5
    elif keys[pygame.K_d] and monsterPosition.x < wall:
        monsterPosition.x += 5


    if monsterPosition.colliderect(breadPosition):
        score += 1
        myScore = myFont.render(f"Score: {score}", True, (222, 222, 222))
        if score == 10:
            monsterImg = pygame.image.load("monster 32.png")
            breadImg = pygame.image.load("bread 32.png")
            wall = 608
            levelUp.play()
        elif score == 20:
            monsterImg = pygame.image.load("monster 64.png")
            breadImg = pygame.image.load("bread 64.png")
            wall =576
            levelUp.play()
        elif score == 30:
            monsterImg = pygame.image.load("monster 128.png")
            breadImg = pygame.image.load("bread 128.png")
            wall = 512
            levelUp.play()
        elif score == 40:
            youWin()
        else:
            collectBread.play()
        breadPosition = placeBread()



    screen.fill((244,244,244))
    screen.blit(monsterImg, monsterPosition)
    screen.blit(breadImg, breadPosition)
    pygame.draw.line(screen, (39, 215, 255), (0,672), (640,672), 75)
    screen.blit(myScore, scorePosition)
    pygame.display.update()
    clock.tick(60)

pygame.quit()