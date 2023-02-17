import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as fps


pygame.init() #init guv


#game veriables related tobehind the sceen stuff
ww = 800
wh = 600
refresh = 30
time = fps.Clock()
start = False
level = 1


#defining names for the objects used in the game
player = pygame.Rect(350, 420, 70, 130)
info = pygame.Rect(0, 0, 800, 600)
honey = pygame.Rect(250, 100, 70, 70)
honey1 = pygame.Rect(350, 100, 70, 70)
honey2 = pygame.Rect(450, 100, 70, 70)
exp = pygame.Rect(20,20 , 0, 40)
bear = pygame.Rect(7000, 100, 70, 130)
item = pygame.Rect(80, 485, 70, 65)
big_barrel = pygame.Rect(620, 465, 100, 85)


#player verables
holding = 1

#honey bucket
honey_bucket = 0
barrel = 0

#veriables ued to set howlong the event loops are
down = 1000
bear_come = 550

#bear veriables
bear_home = True


#event stuff....didt make this comment in time allready forgotten
down_event = pygame.USEREVENT + 1
bear_event = pygame.USEREVENT + 2

pygame.time.set_timer(down_event, down)
pygame.time.set_timer(bear_event, bear_come)


#setting the window size and name
window = pygame.display.set_mode((ww,wh))
pygame.display.set_caption("honeygame")

def bearmove(): #bear brain
    global bear_home, holding

    if bear_home == False:
        bear.x = 680

    if bear.y >= 400:
        bear.y = 400
        
    if bear.y == 400 and player.x == 550 and holding == 2:
        bear_home = True
        holding = 0
        
    if bear_home == True:
        bear.y = 100
        bear.x = 7000


def honeyAI(): #honeybrain....yes...dont argue it
    global honey_bucket, holding

    
    if honey.y == 480:
        honey.y = 100
        exp.width -= 40

    if honey1.y == 480:
        honey1.y = 100
        exp.width -= 40
        
    if honey2.y == 480:
        honey2.y = 100
        exp.width -= 40

    if honey.colliderect(player) and honey_bucket < 3 and holding == 1:
        honey.y = 100
        honey_bucket += 1
        if level < 5:
            exp.width += 40

    if honey1.colliderect(player) and honey_bucket < 3 and holding == 1:
        honey1.y = 100
        honey_bucket += 1
        if level < 5:
            exp.width += 40

    if honey2.colliderect(player) and honey_bucket < 3 and holding == 1:
        honey2.y = 100
        honey_bucket += 1
        if level < 5:
            exp.width += 40

def score():
    global barrel, level
    
    font = pygame.font.Font(None,74) #filename , size
    text = font.render(str(barrel), 1, (255,255,255)) #change colour later when art is added
    tex = font.render(str("score="), 1,(255,255,255))
    level_text = font.render(str(level), 1, (255, 255, 255))
    window.blit(text, (670,10))
    window.blit(tex,(500,10))
    window.blit(level_text, (300,10))

while start is False: #instruction screen

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


while start is True: #game starts here

    window.fill((0,0,0))
    pygame.draw.rect(window, ("yellow"), honey)
    pygame.draw.rect(window, ("yellow"), honey1)
    pygame.draw.rect(window, ("yellow"), honey2)
    pygame.draw.rect(window, ("red"), bear)
    pygame.draw.rect(window, ("blue"), player)
    pygame.draw.rect(window, ("yellow"), exp)
    pygame.draw.rect(window, ("green"), item)
    pygame.draw.rect(window, ("brown"), big_barrel)

    if holding == 0:
        pygame.draw.rect(window, ("yellow"), item)

    if holding == 1:
        pygame.draw.rect(window, ("orange"), item)

    if holding == 2:
        pygame.draw.rect(window, ("purple"), item)

    honeyAI()
    bearmove() #this aint a discord bot dont forget to call your functions
    score()

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
        exp.width = 200

    for event in GAME_EVENTS.get():

        if event.type == bear_event and bear_home == False and bear.y < 400:
            
            bear.y += 50

        if event.type == bear_event and bear.y == 400:

            if player.x != 550 and holding != 2:

                barrel -= 2
                if barrel <= 0:
                    barrel = 0

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
                    b = random.randint(1,4)

                    if b == 4 and bear_home == True:
                        
                        bear_home = False
                
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
            if event.key == pygame.K_LEFT:
                
                if player.x == 150 and holding == 1:
                    holding = 2

                if player.x == 150 and holding == 0:
                    holding = 1

            
            if event.key == pygame.K_RIGHT:

                if player.x == 550 and honey_bucket > 0:
                    barrel += honey_bucket
                    honey_bucket = 0


        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    time.tick(refresh)
        
