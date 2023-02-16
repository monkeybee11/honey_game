import pygame, sys, random, os, io
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as fps


pygame.init()

ww = 800
wh = 600
refresh = 30
time = fps.Clock()
start = False

player = pygame.Rect(150, 420, 70, 130)
info = pygame.Rect(0, 0, 800, 600)
honey = pygame.Rect(250, 100, 70, 70)
honey1 = pygame.Rect(350, 100, 70, 70)
honey2 = pygame.Rect(450, 100, 70, 70)
exp = pygame.Rect(20,20 , 0, 40)
bear = pygame.Rect(7000, 100, 70, 90)

#honey bucket
honey_bucket = 0
barrel = 0
level = 1

#honey movement in milla seccons
down = 1000
bear_come = 100000


down_event = pygame.USEREVENT + 1
bear_event = pygame.USEREVENT + 2

pygame.time.set_timer(down_event, down)
pygame.time.set_timer(bear_event, bear_come)

window = pygame.display.set_mode((ww,wh))
pygame.display.set_caption("honeygame")

def bearmove():
    global bear_come

    if bear_come == 500:
        bear.x = 700
    if bear.y == 420 and player.x == 550:
        bear_come = 100000
    if bear_come == 100000:
        bear.y = 100
        bear.x = 7000


def honeyAI():
    global honey_bucket

    
    if honey.y == 480:
        honey.y = 100
        exp.width -= 40

    if honey1.y == 480:
        honey1.y = 100
        exp.width -= 40
        
    if honey2.y == 480:
        honey2.y = 100
        exp.width -= 40

    if honey.colliderect(player) and honey_bucket < 3:
        honey.y = 100
        honey_bucket += 1
        if level < 5:
            exp.width += 40

    if honey1.colliderect(player) and honey_bucket < 3:
        honey1.y = 100
        honey_bucket += 1
        if level < 5:
            exp.width += 40

    if honey2.colliderect(player) and honey_bucket < 3:
        honey2.y = 100
        honey_bucket += 1
        if level < 5:
            exp.width += 40

while start is False:

    window.fill((0,0,0))
    pygame.draw.rect(window, ("purple"), info)


    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start = True
                
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    time.tick(refresh)


while start is True:

    window.fill((0,0,0))
    pygame.draw.rect(window, ("yellow"), honey)
    pygame.draw.rect(window, ("yellow"), honey1)
    pygame.draw.rect(window, ("yellow"), honey2)
    pygame.draw.rect(window, ("red"), bear)
    pygame.draw.rect(window, ("blue"), player)
    pygame.draw.rect(window, ("yellow"), exp)

    if level == 5:
        exp.width = 200

    honeyAI()

    if level == 1:
        down = 1000

    elif level == 2:
        down = 800
        
    elif level == 3:
        down = 600
        
    elif level == 4:
        down = 400
        
    elif level == 5:
        down = 200

    for event in GAME_EVENTS.get():

        if event.type == bear_event:
            bear.y += 50

        if event.type == down_event:

            if exp.width >= 201:
                exp.width = 0
                level += 1
                if level >= 5:
                    level = 5

            if exp.width < 0:
                exp.width = 0
                level -= 1
                
            a = random.randint(1,7)
            
            if a == 1:
                honey.y += 20
                
            if a == 2:
                honey1.y += 20
                if barrel >= 5:
                    b = random.randint(1,5)
                    print("bear")

                    if b == 5:
                        bear_come = 500
                        print("BEAR")
                
            if a == 3:
                honey2.y += 20
                
            if a == 4:
                honey.y += 20
                honey1.y += 20
                
            if a == 5:
                honey.y += 20
                honey2.y += 20
                
            if a == 6:
                honey1.y += 20
                honey2.y += 20
                
            if a == 7:
                honey1.y += 20
                honey2.y += 20
                honey.y += 20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
                if player.x > 150 and player.x -5 > 150:
                    player.x -= 100
                elif player.x > 150 and player.x -5 < 150:
                    player.x = 0
                    
            if event.key == pygame.K_RIGHT:

                if player.x + player.width < 550 and (player.x + player.width) + 5 < 550:
                    player.x += 100
                elif player.x + player.width < 550 and (player.x + player.width) + 5 > 550:
                    player.x = ww - player.width

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:

                if player.x == 550 and honey_bucket > 0:
                    barrel += honey_bucket
                    honey_bucket = 0


        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    time.tick(refresh)
        
